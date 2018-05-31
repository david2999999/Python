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
            raise TypeError("No such omelet type: %s" % omelet_type)

    # You can check the parameters that are passed in and use raise ... to indicate that the wrong type was
    # given. When you use raise ... , you provide a message that an except ... : clause can capture for
    # display — an explanation of the error.
    # The following code changes the end of the make_omelet function by replacing a printed error, which is
    # suitable for being read by a person running the program, with a raise ... statement that makes it
    # possible for a problem to be either handled by functions or printed so that a user can read it


    def make_food(ingredients_needed, food_name):
        """make_food() takes ingredients from ingredients_needed and make food_name"""
        for ingredient in ingredients_needed.keys():
            print("Adding %d of %s to make a %s" % (ingredients_needed[ingredient], ingredient, food_name))
            print("Made %s " % food_name)
            return food_name
if __name__ == "__main__":
    main()