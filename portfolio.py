from dataclass import dataclass


@dataclass
class Position:
    instrument: Instrument
    quanity: float

    def get_value(self):



@dataclass
class Portfolio:
    cash: float
    positions: dict[str, Position]



    def buy(self, instrument: Instrument, quanity: float, market_price: float):
        if self.cash < market_price:
            return False
        
        
    def sell(self, instrument: Instrument, quanity: float, market_price: float):
