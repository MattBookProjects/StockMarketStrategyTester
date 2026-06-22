from abc import ABC, abstractmethod
from dataclasses import dataclass

class Action(ABC):


    @abstractmethod
    def apply(self, execution_model: ExecutionModel):
        pass



@dataclass
class TradeStockAction(Action):
    symbol: str
    volume: float
    transaction_spec: TransactionSpecification
 

    def apply(self, execution_model: ExecutionModel):
        execution_model.send_order(StockOrder{symbol: symbol, volume: volume, transaction_spec: transaction_spec})




@dataclass
class TradeOptionAction(Action):
    contract: OptionContract
    quantity: int
    transaction_spec: TransactionSpecification


   
    def apply(self, execution_model: ExecutionModel):
        execution_model.send_order(OptionOrder{contract: contract, quantity: quantity, transaction_spec: transaction_spec}) 

@dataclass
class ExcerciseOptionInstructionAction(Action):
    contract: OptionContract
    
  
    def apply(self, execution_model: ExecutionModel):
        execution_model.schedule_excercising_option(self.contract)

@dataclass
class CancelExcercisingOptionAction(Action):
    contract_id: str
    

    def apply(self, execution_model: ExecutionModel):
        execution_model.cancel_excercising_option(self.contract_id)

@dataclass
class CancelOrderAction(Action):
    order_id: str

    def apply(self, execution_model: ExecutionModel):
        execution_model.cancel_order(order_id)
    

@dataclass
class TransactionSpecification:
    side: TransactionSide
    order_type: OrderType
    order_specification: OrderSpecification


    def get_payload(self):
        payload {
            "side": self.side,
            "order_type": self.order_type
        }






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