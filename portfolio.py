from dataclasses import dataclass
from abc import ABC, abstractmethod


class MarketValue(ABC):
    pass

@dataclass
class StockMarketValue(MarketValue):
    price: float





class Position(ABC):
    
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
class StockPosition(Position):
    name: str
    quanity: float

    def __eq__(self, obj):
        return isinstance(obj, StockPosition) and self.name == obj.name
    
    def __add__(self, obj):
        self.quanity += obj.quanity


    def __sub__(self, obj):
        self.quanity -= obj.quanity

    def get_value(self, market_value):
        if not isinstance(market_value, StockMarketValue):
            raise TypeError
        return self.quanity * market_value.price 

@dataclass
class Portfolio:
    cash: float
    positions: list[Position]


    def __init__(self, cash, positions=[]):
        self.cash = cash
        self.position = positions

    def buy(self, postion: Position, market_value: MarketValue):
        position_value =  position.get_value(market_value):
        if position_value > self.cash:
            return False
        self.cash -= position_value
        try:
            index = self.positions.index(position)
            self.positions[index] += position
        except ValueError as err:
            self.positions.append(position)
        finally:
            return True
            
        
        
    def sell(self, position: Position, market_value: MarketValue):
        try:
            index = self.positions.index(position)
            held_position = self.positions[index]
            if position > held_position:
                return False
            position_value = postion.get_value(market_value)
            held_position -= position
            self.cash += position_value
        except ValueError:
            return False

        
    def sell_whole_stock(self, stock: str):
        try:
            index = self.positions.index(Stock(name=stock))
            held_position = self.positions[index]




if __name__=='__main__':
    aapl = StockPosition("AAPL", 10)
    aapl2 = StockPosition("AAPL", 20)
    aapl_total = aapl + aapl2
    print(f"name: {aapl_total.name}\tquanity: {aapl_total.quanity}")