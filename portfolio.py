from dataclasses import dataclass
from abc import ABC, abstractmethod





class PortfolioPosition(ABC):
    
    @abstractmethod
    def get_value(self, market_value):
        pass

    @abstractmethod
    def __eq__(self, obj):
        pass

    @abstractmethod
    def __add__(self, obj):
        pass

    @abstractmethod
    def __sub__(self, obj):
        pass


@dataclass
class StockPosition(PortfolioPosition):
    symbol: str
    quanity: float


    def __init__(self, symbol, quanity):
        self.symbol = symbol
        self.quanity = quanity

    def __eq__(self, obj):
        return isinstance(obj, StockPosition) and self.symbol == obj.symbol
    
    def __add__(self, obj):
        if self != obj:
            raise TypeError
        return StockPosition(self.symbol, self.quanity + obj.quanity)


    def __sub__(self, obj):
        if self != obj:
            raise TypeError
        return StockPosition(self.symbol, self.quanity - obj.quanity)

    def get_value(self, market_value):
        if not isinstance(market_value, StockMarketValue):
            raise TypeError
        return self.quanity * market_value.price


@dataclass
class OptionPosition(PortfolioPosition):
    contract: OptionContract
    quanity: int 

    def __init__(self, contact, quanity):
        self.contact = contact
        self.quanity = quanity

    def __eq__(self, obj):
        return isinstance(obj, OptionPosition) and self.contract == obj.contract

    def __add__(self, obj):
        if self != obj:
            raise TypeError
        return OptionPosition(self.contact, self.quanity + obj.quanity)

    def __sub__(self, obj):
        if self != obj:
            raise TypeError
        return OptionPosition(self.contact, self.quanity - obj.quanity)

    def get_value(self, market_value):
        pass

        

@dataclass
class Portfolio:
    cash: float
    positions: list(Position)


    def __init__(self, cash, positions=[]):
        self.cash = cash
        self.positions = positions

    def reduce_position(self, postion: Position):
        try:
            pos_idx = self.positions.index(position)
            self.posiotions[pos_idx] -= position
        except ValueError:
            print("Not enough instrument in portfolio")

    def increase_position(self, posotion: Position)
        try:
            pos_idx = self.posistions.index(position)
            self.posistions[pos_idx] += position
        except ValueError:
            self.positions.append(position)
        


    def add_cash(self, amount):
        self.cash += cash
        
    def substract_cash(self, amount):
        self.cash -= cash




if __name__=='__main__':
    pass