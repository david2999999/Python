import sys
from Archive.PDF.Modules import Foods

# You now have access to the Fridge class, the Omelet class and, from the previous exercises, the Recipe
# class. Together, you have a file that is a module that contains all of these classes, and they ’ ll be able to
# work together. However, you ’ ll now access them through the name Foods.Fridge , Foods.Omelet , and
# Foods.Recipe , and they remain fully usable, albeit with some new rules.
from Archive.PDF.Modules.Foods import Recipe, Omelet


def main():
    print(dir(Foods))
    print(Foods.Fridge)
    print(Foods.Omelet)

    print("This was given the command line parameters: %s" % sys.argv)

    r = Foods.Recipe()
    onion_ingredients = Foods.Omelet(r, "onion")

    # You can see by this example that when you want to invoke or access something inside of a module, it
    # means spelling out the entire path. You can quickly tire of doing this. However, you can change this
    # behavior by bringing the names you want closer into your code by using the from modifier to the
    # import command:
    recipe = Recipe()
    new_onion = Omelet(r, "onion")

if __name__ == "__main__":
    main()

    # dir will show you even more than the helpful dialog
    # box in the Code Editor shell, because it shows private names that aren ’ t part of the interface of the
    # module. These concepts, which you ’ ve seen in classes and objects, still apply to modules!)