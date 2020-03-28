# In fact, sometimes it ’ s useful to have this
# method be considered private , or not a part of the interface. This way it can be used or not used and
# changed without affecting how the class is used, because any changes you make will not be seen
# outside an object, only inside .
# For your Fridge class, you can minimize your work by creating an internal method called _add_multi
# that will take two parameters — the name of the item and the quantity of items — and have it add
# those to the items dictionary that each object has.
def main():
    class Fridge:
        def __init__(self, items={}):
            """Optionally pass in an initial dictionary of items"""
            if type(items) != type({}):
                raise TypeError("Fridge requires a dictionary but was given %s" % type(items))
            self.items = items
            return

        def __add_multi(self, food_name, quantity):
            """add_multi(food_name, quantity) - adds more than one of a
            food item. Returns the number of items added. This should only be used
            internally, after the type checking has been done"""
            if not food_name in self.items:
                self.items[food_name] = 0

            self.items[food_name] = self.items[food_name] + quantity



if __name__ == "__main__":
    main()