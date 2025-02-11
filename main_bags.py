from BigBag import BigBag

if __name__ == "__main__":
    from SmallBag import SmallBag
    from Food import Food# Move the import here to avoid circular import

    health_bag = SmallBag("Health Bag")
    candy_bag = SmallBag("Candy Bag")
    bread = Food("Bread", 1.3)
    cheese = Food("Cheese", 0.5)
    water = Food("Water", 3.5)
    corn = Food("Corn", 1.6)
    bamba = Food("Bamba", 0.25)
    bisly = Food("Bisly", 0.3)
    marshmello = Food("Marshmello", 0.4)

    health_bag.add_food(bread)
    health_bag.add_food(cheese)
    health_bag.add_food(corn)

    candy_bag.add_food(water)
    candy_bag.add_food(bisly)
    candy_bag.add_food(bamba)
    candy_bag.add_food(marshmello)

    print(candy_bag.get_weight())
    print(health_bag.get_weight())
    print(f"{candy_bag.get_weight()+health_bag.get_weight()}")

    print(candy_bag)


    total_weight = candy_bag.get_weight()+health_bag.get_weight()
    print(f"The total weight in the Big Bag is {total_weight}")
    print(candy_bag.get_food())
    print()
    print(candy_bag.get_weight())
    print(total_weight)

    print(f"Total weight in Candy Bag is: {candy_bag.get_weight()} kg")
    print(f"Total weight in Health Bag is: {health_bag.get_weight()} kg")
    print(f"Combined total weight: {candy_bag.get_weight() + health_bag.get_weight()} kg")
    print(candy_bag)
    print(health_bag.get_food())