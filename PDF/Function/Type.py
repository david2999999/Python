# To determine the type of some data, remember that you can use the type built - in function, which was
# introduced in Chapter 2. Using the output of this, you can verify the type of variable in the beginning of
# your functions:
def main():
    def make_omelet(omelet_type):
        """This will make an omelet. You can either pass in a dictionary that containst
        all of the ingredients for your omelet, or provide a string to select a type
        of omelet this function already knows about"""
        if type(omelet_type) == type({}):
            print("omelet_type is a dictionary with ingredients")
            return make_food(omelet_type, "omelet")
        elif type(omelet_type) == type(""):
            omelet_ingredients = get_omelet_ingredients(omelet_type)
            return make_food(omelet_ingredients, omelet_type)
        else:
            print("I don't think I can make this kind of Omelet: %s" % omelet_type)

    # currently incomplete function
    def make_food(ingredients_needed, food_name):
        """make_food() takes ingredients from ingredients_needed and make food_name"""
        for ingredient in ingredients_needed.keys():
            print("Adding %d of %s to make a %s" % (ingredients_needed[ingredient], ingredient, food_name))
            print("Made %s " % food_name)
            return food_name

    def get_omelet_ingredients(omelet_name):
        """This contains a dictionary of omelet names that can be produced, and their ingredients"""
        # All of our omelet needs eggs and milk
        ingredients = {"eggs" : 2, "milk": 1}
        if omelet_name == "cheese":
            ingredients["cheddar"] = 2
        elif omelet_name == "western":
            ingredients["jack_cheese"] = 2
            ingredients["ham"] = 2
            ingredients["pepper"] = 1
            ingredients["onion"] = 1
        elif omelet_name == "greek":
            ingredients["feta_cheese"] = 2
            ingredients["spinach"] = 2
        else:
            print("That's not on the menu sorry")
            return None

        return ingredients




if __name__ == "__main__":
    main()

    # Functions declared within the top level, or global scope, can be used from within other functions and
    # from within the functions inside of other functions. The names in the global scope can be used from
    # everywhere, because the most useful functions need to be available for use within other functions.