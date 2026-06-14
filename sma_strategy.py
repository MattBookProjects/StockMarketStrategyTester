from strategy import Strategy
from collections import deque
import numpy as np
import pandas as pd
from enum import Enum




class SmaStrategy(Strategy):

    class Decision(Enum):
        BUY = 0
        SELL = 1
    

    class InstrumentData:
        def __init__(self, symbol, long_period, short_period):
            self.long_period = long_period
            self.short_period = short_period
            self.symbol = symbol
            self.long_period_data = deque()
            self.short_period_data = deque()
            self.current_data_count = 0
            self.long_avg = None
            self.short_avg = None
            self.old_long_avg = None
            self.old_short_avg = None

        def process_new_data(self, new_price):
            print("TYPEOF NEW PRICE")
            #print(type(new_price))
            if self.long_avg is not None:
                self.old_long_avg = self.long_avg
                #print(f"currend_old_long_avg: {self.old_long_avg}")
            if self.short_avg is not None:
                self.old_short_avg = self.short_avg
                #print(f"current_old_short_avg: {self.old_short_avg}")

            if self.current_data_count == self.long_period:
                #print(type(self.long_period_data))
                long_removed = self.long_period_data.popleft()
                #print(type(long_removed))
                print(f"long_removed: {long_removed}")
                self.long_period_data.append(new_price)
                self.long_avg += (new_price - long_removed)/float(self.long_period)
                short_removed = self.short_period_data.popleft()
                print(f"short_removed: {short_removed}")
                self.short_period_data.append(new_price)
                self.short_avg += (new_price - short_removed)/float(self.short_period)

            elif self.current_data_count >= self.short_period:
                short_removed = self.short_period_data.popleft()
                self.short_period_data.append(new_price)
                self.short_avg + (new_price - short_removed)/self.short_period
                self.long_period_data.append(new_price)
                self.current_data_count += 1
                if self.current_data_count == self.long_period:
                    self.long_avg = np.array(self.long_period_data, dtype=float).mean()
                    print(f"Long avg calculated: {self.long_avg}")

            else:
                self.short_period_data.append(new_price)
                self.long_period_data.append(new_price)
                self.current_data_count += 1
                if self.current_data_count == self.short_period:
                    self.short_avg = np.array(self.short_period_data, dtype=float).mean()
                    print(f"Short avg calculated: {self.short_avg}")



        def has_enough_data(self):
            return self.old_long_avg is not None and self.old_short_avg is not None

        
        def get_averages(self):        
            return np.array([[self.old_long_avg, self.old_short_avg], [self.long_avg, self.short_avg]])


   


    def __init__(self, instruments, long_period, short_period):
        self.instruments = instruments
        self.instruments_data = {sym: self.InstrumentData(sym, long_period, short_period) for sym in instruments}
        self.long_period = long_period
        self.short_period = short_period


    def process_new_data(self, data):
        #print(type(data))
        #print(f"processing data: {data}")
        considered_instruments = data[self.instruments]
        #print(type(considered_instruments))
        print(f"conisdered instrument: {considered_instruments}")
        averages = dict()
        #print("SO FAR SO GOOD SO WHAT")
        print(type(considered_instruments))
        for col in considered_instruments.columns:
            instr_data = self.instruments_data[col]
            print("type of instr_data")
            print(type(instr_data))
            instr_data.process_new_data(considered_instruments[col].iloc[0])
            if instr_data.has_enough_data():
                avg = instr_data.get_averages()
                print(f"AVERAGE: {avg}")
                averages[col] = avg
        print(f"averages: {averages}")
        to_buy = {"name" : [], "ratio": []}
        to_sell = {"name" : [], "ratio": []}
        for col in averages:
            decision = self.make_decision_from_averages(averages[col])
            if decision is None:
                continue
            elif decision[0] == Decision.BUY:
                to_buy["name"].append(col)
                to_buy["ratio"].append(decision[1])
            elif decision[0] == Decision.SELL:
                to_sell["name"].append(col)
                to_sell["ratio"].append(decision[1])
        df_buy = pd.DataFrame(data=to_buy).sort_values(by="ratio")
        df_sell = pd.DataFrame(data=to_sell).sort_values(by="ratio", ascending=True)
        return {
            "buys": df_buy,
            "sells": df_sell
        }


    def make_decision_from_averages(self, averages):
        rate = (averages[1][1] - averages[1][0]) - (averages[0][1] - averages[0][0])
        if averages[0][0] > averages[0][1] and averages[1][0] <= averages[1][1]:
            return (Decision.BUY, rate)
        elif averages[0][0] < averages[1][0] and averages[1][0] >= averages[1][1]:
            return (Decision.SELL, rate)
        else:
            return None




def main(symbols, data):
    strat = SmaStrategy(symbols, 50, 20)
    #print(strat.instruments)
    for idx in range(len(data)):
        df = data.iloc[[idx]]
        strat.process_new_data(df)
    




if __name__=='__main__':
    symbols = ['AAPL']
    data = [
       {"AAPL": 4} for i in range(50)
    ]
    data.extend([{"AAPL": 4.5} for i in range(50)])
    df = pd.DataFrame(data=data)
    print(df)
    main(symbols, df)