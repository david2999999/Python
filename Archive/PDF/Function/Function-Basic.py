# This is more than just useful — it makes sense and it saves you work. This grouping of blocks of code
# under the cover of a single name means that you can now simplify your code, which in turn enables you
# to get more done more quickly. You can type less and worry less about making a mistake as well.
# Functions are a core part of any modern programming language, and they are a key part of getting
# problems solved using Python.
def main():
    def in_fridge():
        try:
            count = fridge[wanted_food]
        except KeyError:
            count = 0

        return count


    fridge = {'apple': 10, 'oranges': 3, 'milk': 2}

    wanted_food = 'apple'
    print("%d" % in_fridge())

    wanted_food = 'oranges'
    print("%d" % in_fridge())

    wanted_food = 'milk'
    print("%d" % in_fridge())

if __name__ == "__main__":
    main()