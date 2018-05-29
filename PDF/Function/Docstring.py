# If you place a string as the first thing in a function, without referencing a name to the string, Python will
# store it in the function so you can reference it later. This is commonly called a docstring , which is short for
# documentation string .
# Documentation in the context of a function is anything written that describes the part of the program
# (the function, in this case) that you ’ re looking at. It ’ s famously rare to find computer software that is well
# documented. However, the simplicity of the docstring feature in Python makes it so that, generally,
# much more information is available inside Python programs than in programs written in other
# languages that lack this friendly and helpful convention.
# The text inside the docstring doesn’t necessarily have to obey the indentation rules that the rest of the
# source code does, because it ’ s only a string. Even though it may visually interrupt the indentation, it ’ s
# important to remember that, when you ’ ve finished typing in your docstring, the remainder of your
# functions must still be correctly indented.
def main():
    def in_fridge():
        """This is a function to see if the fridge has a food.
        fridge has to be a dictionary defined outside of the function.
        the food to be searched for is in the string wanted_food"""
        try:
            count = fridge[wanted_food]
        except KeyError:
            count = 0

        return count


    fridge = {'apple': 10, 'oranges': 3, 'milk': 2}

    wanted_food = 'apple'
    print("%d" % in_fridge())

    print("%s" % in_fridge.__doc__)

if __name__ == "__main__":
    main()