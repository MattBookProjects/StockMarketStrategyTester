from abc import ABC, abstractmethod



class ExecutionModel(ABC):
    
    @abstractmethod
    def send_order(self, order: Order):
        pass

    @abstractmethod
    def cancel_order(self, order_id: str):
        pass

    @abstractmethod
    def schedule_excercising_option(self, contract):
        pass
    
    @abstractmethod
    def cancel_excercising_option(self, contract_id):
        pass
