from execution_model import ExecutionModel



class SimulationExecutionModel(ExecutionModel):

    def __init__(self, simulation_engine: SimulationEngine):
        self.engine = simulation_engine

    @abstractmethod
    def send_order(self, order: Order):
        self.engine.send_order(order)

    @abstractmethod
    def cancel_order(self, order_id: str):
        self.enging.cancel_order(self, order_id)

    @abstractmethod
    def schedule_excercising_option(self, contract):
        self.engine.schedule_excercising_option(self, contract)
        pass
    
    @abstractmethod
    def cancel_excercising_option(self, contract_id):
        self.engine.cancel_excercising_option(self, contract_id)
        pass
