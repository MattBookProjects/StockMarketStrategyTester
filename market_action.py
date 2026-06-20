from abc import ABC, abstractmethod

class MarketAction(ABC):

    @abstractmethod
    def execute(self, portfolio):
        pass


if __name__ == '__main__':
    print("Works")