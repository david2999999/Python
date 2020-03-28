def main():
    # Equality isn ’ t the only way to find out what you want to know. Sometimes you will want to know
    # whether a quantity of something is greater than that of another, or whether a value is less than
    # some other value. Python has greater than and less than operations that can be invoked with the >
    # and < characters, respectively. These are the same symbols you are familiar with from math books, and
    # the question is always asking whether the value on the left is greater than ( > ) or less than ( < ) the value
    # on the right .
    print(5 < 3)
    print(10 > 2)

    # The number on the left is compared to the number on the right. You can compare letters, too. A few
    # conditions exist where this might not do what you expect, such as trying to compare letters to
    # numbers. (The question just doesn ’ t come up in many cases, so what you expect and what Python
    # expects is probably not the same.) The values of the letters in the alphabet run roughly this way: A
    # capital “ A ” is the lowest letter. “ B ” is the next, followed by “ C ” and so on until “ Z ” . This is followed
    # by the lowercase letters, with “ a ” being the lowest lowercase letter and “ z ” the highest. However, “ a ”
    # is higher than “ Z ” :
    print("a" > "b")
    print("A" > "b")
    print("A" > "a")
    print("b" > "A")
    print("Z" > "a")

    #     If you want to compare two strings that are longer than a single character, Python will look at each
    # letter until it finds one that ’ s different. When that happens, the outcome will depend on that one
    # difference. If the strings are completely different, the first letter will decide the outcome:
    print("Zebra" > "aardvark")
    print("Zebra" > "Zebrb")
    print("Zebra" < "Zebrb")

    #     You can avoid the problem of trying to compare two words that are similar but have differences in
    # capitalization by using a special method of strings called lower , which acts on its string and returns a
    # new string with all lowercase letters. There is also a corresponding upper method. These are available
    # for every string in Python:
    print("Pumpkin" == "pumpkin")
    print("Pumpkin".lower() == "pumpkin".lower())
    print("Pumpkin".lower())
    print("Pumpkin".upper() == "pumpkin".upper())

if __name__ == "__main__":
    main()