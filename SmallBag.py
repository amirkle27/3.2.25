from typing import override
from BigBag import BigBag

class SmallBag(BigBag):

    def __init__(self, food):
        super().__init__(food)
        self.foods = []

    @override
    def add_food(self,food):
        self.foods.append(food)

    @override
    def remove_food(self,food):
        self.foods.remove(food)

    @override
    def get_food(self):
        food_list =', '.join(str(food) for food in self.foods)
        return f"{self.bag} contains: {food_list}"

    @override
    def get_weight(self):
        total_weight = sum(food.get_weight() for food in self.foods)
        return f"{total_weight:.2f}"

