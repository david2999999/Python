# The methods that an object makes available for use are called its interface because these methods are
# how the program outside of the object makes use of the object. They ’ re what make the object usable.
# The interface is everything you make available from the object. With Python, this usually means that
# all of the methods and any other names that don ’ t begin with one or more underscores are your
# interfaces; however, it ’ s a good practice to distinguish which functions you expect to have called by
# explicitly stating what methods can be used, and how they ’ re used, in the class ’ s docstring:
def main():
    class fridge:
        """This class implements a fridge where ingredients can be added and removed individually,
        or in group. The fridge will retain a count of every ingredient added or removed, and will
        raise an error if a sufficient quantity of an ingredient isn't present
        Methods:
            has(food_name [, quantity]) - checks if the string food_name is in the
                            fridge. Quantity will be set to 1 if you don’t specify a number.
            has_various(foods) - checks if enough of every food in the dictionary is in
                                the fridge
            add_one(food_name) - adds a single food_name to the fridge
            add_many(food_dict) - adds a whole dictionary filled with food
            get_one(food_name) - takes out a single food_name from the fridge
            get_many(food_dict) - takes out a whole dictionary worth of food.
            get_ingredients(food) - If passed an object that has the __ingredients__
                                        method, get_many will invoke this to get the list of ingredients."""

        def __init__(self, items={}):
            """Optionally pass in an initial dictionary of items"""
            if type(items) != type({}):
                raise TypeError("Fridge requires a dictionary but was given %s" % type(items))
            self.items = items
            return


if __name__ == "__main__":
    main()

    # Take a moment to look at the __init__ and (self) part of the code above. These are two very important
    # features of classes. When Python creates your object, the __init__ method is what passes the object its
    # first parameter. The (self) portion is actually a variable used to represent the instance of the object.