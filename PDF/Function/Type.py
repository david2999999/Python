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

    def make_food(omelet_type, food):
        print(str(omelet_type) + food)

    def get_omelet_ingredients(omelet, food):
        return omelet[food]

if __name__ == "__main__":
    main()

    # By itself, this definition of make_omelet won ’ t work because it relies on a few functions that you
    # haven ’ t written yet. You will sometimes do this as you program — create names for functions that need
    # to be written later. You ’ ll see these functions later in this chapter, at which point this code will become
    # fully usable.