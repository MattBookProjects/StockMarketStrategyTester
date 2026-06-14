class BankrollManagementStrategy:
    def __init__(self, portfolio):
        self.portfolio = portfolio
    
    @abstractmethod
    def calculate_transactions_volumes(self, data):
        pass




class SimpleBankrollManagementStrategy(BankrollManagementStrategy):


    def calculate_transactions_volumes(self, data):
        buys = data["buys"]
        sells = data["sells"]

        transactions = []
        current_cash = self.portfolio.cash
        for pos in buys:
            transactions.append(pos["name"])