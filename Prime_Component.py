from abc import abstractmethod, ABC

class PrimeComponent(ABC):

    def __init__(self):
        self.next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self,value):
        self.__next = value

    @abstractmethod
    def prime_checker(self,number):
        pass





