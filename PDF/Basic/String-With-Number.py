# When you combined two strings in the first chapter by using a format specifier, you used the format
# specifier %s , which means “ a string. ” Because numbers and strings have different types, you will use a
# different specifier that will enable your numbers to be included in a string
def main():
    print("Including an integer to works with %%d like this: %d" % 10)
    print("An integer converted to a float with %%f: %f" % 5)
    print("A normal float with %%f: %f" % 1.2345)
    print("A really large number with %%E: %E" % 6.789E10)
    print("Controlling the number of decimal places shown: %.02f" % 25.10100101010)

    # One other trick was shown before. If you want to print the literal string %d in your program, you
    # achieve that in Python strings by using two % signs together. This is needed only when you also have
    # valid format specifiers that you want Python to substitute for you in the same string


    print("%f" % (5/3))
    print("%.2f" % (5/3))
    print("%f" % (415 * 20.2))
    print("%0.f" % (415 * 20.2))


if __name__ == "__main__":
    main()