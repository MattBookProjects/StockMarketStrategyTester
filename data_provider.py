from abc import ABC, abstractmethod

class DataProvider(ABC):

    @abstractmethod
    def emit_data(self):
        pass



if __name__ == '__main__':
    print("Works")