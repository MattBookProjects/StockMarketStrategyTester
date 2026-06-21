from abc import ABC, abstractmethod
from dataclasses import dataclass

class Action(ABC):


    @abstractmethod
    def apply(self):
        pass



@dataclass
class TradeStockAction(Action):
    symbol: str
    volume: float
    transaction_spec: TransactionSpecification
 




    def apply(self):
        pass




@dataclass
class TradeOptionAction(Action):
    contract: OptionContract
    quantity: int
    transaction_spec: TransactionSpecification


   


    def apply(self):
        pass 

@dataclass
class ExcerciseOptionInstructionAction(Action):
    contract: OptionContract
  



    def apply(self):
        pass


    

@dataclass
class TransactionSpecification:
    side: TransactionSide
    order_type: OrderType
    order_specification: OrderSpecification




if __name__ == '__main__':
    print("Works")


def transaction_side_to_payload(side: TransactionSide):
    if side == BUY:
        return {
            "side": "BUY"
        }
    elif side == SELL:
        return {
            "side": "SELL"
        }
    else:
        raise ValueError