# Defining a function within another function looks exactly like defining it at the top level. The only
# difference is that it is indented at the same level as the other code in the function in which it ’ s contained.

# You may decide that a particular function ’ s work is too much to define in one place and want to break it
# down into smaller, distinct pieces. To do this, you can place functions inside of other functions and
# have them invoked from within that function. This allows for more sense to be made of the complex
# function. For instance, get_omelet_ingredients could be contained entirely inside the make_
# omelet function and not be available to the rest of the program.
def main():
    def make_omelet(omelet_type):
        """This will make an omelet, you can either pass in a dictionary that contains all of the ingredients for your omelet
        , or provide a string to select a type of omelet this function already knows about"""

        def get_omelet_ingredients(omelet_name):
            """This contains a dictionary of omelets name that can be produced, and their ingredients"""
            ingredients = {"eggs": 2, "milk": 1}
            if omelet_name == "cheese":
                ingredients["cheddar"] = 2
            elif omelet_name == "western":
                ingredients["jack cheese"] = 2
                ingredients["ham"] = 1
                ingredients["pepper"] = 1
                ingredients["onion"] = 1
            elif omelet_name == "greek":
                ingredients["feta cheese"] = 2
            else:
                print("That's not on the menu, sorry")
                return None
            return ingredients

        if type(omelet_type) == type({}):
            print("omelet_type is a dictionary with ingredients")
            return make_food(omelet_type, "omelet")
        elif type(omelet_type) == type(""):
            omelet_ingredients = get_omelet_ingredients(omelet_type)
            return make_food(omelet_ingredients, omelet_type)
        else:
            print("I don't think I can make this kind of omelet: %s" % omelet_type)


    def make_food(ingredients_needed, food_name):
        """make_food() takes ingredients from ingredients_needed and make food_name"""
        for ingredient in ingredients_needed.keys():
            print("Adding %d of %s to make a %s" % (ingredients_needed[ingredient], ingredient, food_name))
            print("Made %s " % food_name)
            return food_name
if __name__ == "__main__":
    main()

    # It is important to define a function before it is used. If an attempt is made to invoke a function before it ’ s
    # defined, Python won ’ t be aware of its existence at the point in the program where you ’ re trying to
    # invoke it, and so it can ’ t be used! Of course, this will result in an error and an exception being raised. So,
    # define your functions at the beginning of your files so you can use them toward the end.