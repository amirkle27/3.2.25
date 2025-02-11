from abc import ABC, abstractmethod


class BigBag(ABC):

    def __init__(self,bag):
        self.bag = bag

    @abstractmethod
    def add_food(self,food):
        pass

    @abstractmethod
    def remove_food(self,food):
        pass

    @abstractmethod
    def get_food(self):
        pass

    @abstractmethod
    def get_weight(self):
        pass
