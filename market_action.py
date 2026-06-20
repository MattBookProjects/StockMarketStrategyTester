from abc import ABC, abstractmethod

class MarketAction(ABC):

    @abstractmethod
    def execute(self):
        pass


@dataclass
class StockAction(MarketAction):
    symbol: str
    price_levels: list(PriceLevel)

@dataclass
class BuyStockAction(StockAction):

    def execute(self):
        pass


@dataclass
class SellStockAction(StockAction):

    def execute(self):
        pass



if __name__ == '__main__':
    print("Works")