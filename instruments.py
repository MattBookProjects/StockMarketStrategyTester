import numpy as np

@abstractclass
class Instrument:
    pass

@dataclass
class Stock(Instrument):
    symbol: str
    
    def get_value(self, market_price):
        return self.quanity * market_price


    def __init__(self, symbol: str)