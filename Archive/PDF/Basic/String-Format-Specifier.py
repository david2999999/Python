# The %s is known as a format specifier, specifically for strings. As the discussion on data types
# continues throughout this book, you take a look at several more, each specific to its given data type.
# Every specifier acts as a placeholder for that type in the string; and after the string, the % sign outside
# of the string indicates that after it, all of the values to be inserted into the format specifier will be
# presented there to be used in the string.
def main():
    print("Dav Q. %s" % "Public")
    print("Tif %s %s" % ("Every", "Sa"))

    # In the first line of code, the word Man appears far away from the other words; this is because in your
    # last format specifier, you added a 10, so it is expecting a string with ten characters. When it does not
    # find ten (it only finds three . . . M - a - n) it pads space in between with seven spaces.
    print("%s %s %10s" % ("Lua", "Uas", "man"))
    print("%-5s %s %10s" % ("John", "Every", "man"))


if __name__ == "__main__":
    main()