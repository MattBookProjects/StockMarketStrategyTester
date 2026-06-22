from abc import ABC, abstractmethod
from enum import Enum
from dataclasses import dataclass


class OrderInstructions(ABC):
    pass


class MarketOrderInstructions(OrderInstructions):
    pass

@dataclass
class LimitOrdrerInstructions(OrderInstructions):
    limit_price: float

@dataclass
class StopOrderInstructions(OrderInstructions):
    stop_price: float


@dataclass
class StopLimitOrderInstructions(OrderInstructions):
    limit_price: float
    stop_price: float



class TransactionSide(Enum):
    BUY,
    SELL

class OrderType(Enum):
    LIMIT_ORDER,
    MARKET_ORDER
    STOP_ORDER
    STOP_LIMIT_ORDER


class TimeInForce(Enum):
    DAY = "DAY"
    GTC = "GTC",
    IOC = "IOC",
    FOK = "FOK"
    GTD = "GTD"




@dataclass
class Order(ABC):
    transaction_spec: TransactionSpec
    time_in_force: TimeInForce

    @abstractmethod
    def get_payload(self):
        pass


@dataclass
class StockOrder(Order):
    symbol: str
    volume: float
    

    def get_payload(self):
        payload = {"symbol": self.symbol, "volume": self.volume, "time_in_force": self.time_in_force}
        payload.update(self.transaction_spec.get_payload())
        return payload

@dataclass
class OptionOrder(Order):
    contract: OptionContract
    quantity: int

    def get_payload(self):
        payload = {"contract": self.contract, "quanity": self.quanity, "time_in_force": self.time_in_force}
        payload.update(self.transaction_spec.get_payload())
        return payload




@dataclass
class OptionOrder(Order):
    
