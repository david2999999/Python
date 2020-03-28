# Scope defines how available any name is to another part of the program. The scope of a name that ’ s used
# inside of a function can be thought of as being on a vertical scale. The names that are visible everywhere
# are at the top level and they are referred to in Python as being global . Names in any particular function
# are a level below that — a scope that is local to each function. Functions do not share these with other
# functions at the same level; they each have their own scope.
def main():
    special_sauce = ['ketchup', 'mayonnaise', 'french dressing']

    def make_new_sauce():
        """This function makes a new sauce on its own"""
        special_sauce = ["mustard", "yogurt"]
        return special_sauce

    # At this point, there is a special sauce in the top - level scope, and another that is used in the function
    # make_new_sauce . When they are run, you can see that the name in the global scope is not changed:
    print(special_sauce)
    new_sauce = make_new_sauce()

    print(special_sauce)
    print(new_sauce)

if __name__ == "__main__":
    main()