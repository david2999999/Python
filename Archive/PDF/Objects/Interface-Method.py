def main():
    class Fridge:
        def __init__(self, items={}):
            if type(items) != type({}):
                raise TypeError("Fridge requires a dictionary but was given %s" % type(items))
            self.items = items
            return

        def __add_multi(self, food_name, quantity):
            if not food_name in self.items:
                self.items[food_name] = 0

            self.items[food_name] = self.items[food_name] + quantity

        def add_one(self, food_name):
            """add_one(food_name) - adds a single food_name to the fridge returns True
            Raises a TypeError if food_name is not a string"""
            if type(food_name) != type(""):
                raise TypeError("add_one requires a string, given a %s" % type(food_name))
            else:
                self.__add_multi(food_name, 1)

            return True

        def add_many(self, food_dict):
            """add_many(food_dict) - adds a whole dictionary filled with food as keys and quantities
            as values. returns a dictionary with the removed food. raised a TypeError if food_dict
            is not a dictionary return False if there is not enough food in the fridge"""
            if type(food_dict) != type({}):
                raise TypeError("add_many requires a dictionary, got a %s" % food_dict)
            for item in food_dict.keys():
                self.__add_multi(item, food_dict[item])
            return

    f = Fridge({"eggs": 6, "milk": 4, "cheese": 3})
    print(f.items)

    f.add_one("grape")
    print(f.items)

    f.add_many({"mushroom": 5, "tomato" : 3})
    print(f.items)


if __name__ == "__main__":
    main()