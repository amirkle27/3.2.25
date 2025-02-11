from typing import override

from BigBag import BigBag


class Food(BigBag):

    def __init__(self, food: str, weight: float):
        super().__init__(food)
        self.weight = weight
        self.name = food





    def __str__(self):
        return f"{self.get_food()} ({self.weight} kg)"

    @override
    def add_food(self, food):
        pass

    @override
    def remove_food(self, food):
        pass

    @override
    def get_food(self):
        return self.name

    @override
    def get_weight(self):
        return self.weight



