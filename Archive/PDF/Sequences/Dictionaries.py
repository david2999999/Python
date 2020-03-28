def main():
    # When you first assign to menus_specials , you ’ re creating an empty dictionary with the curly braces.
    # Once the dictionary is defined and referenced by the name, you may start to use this style of
    # specifying the name that you want to be the index as the value inside of the square brackets, and the
    # values that will be referenced through that index are on the right side of the equals sign. Because
    # they ’ re indexed by names that you choose, you can use this form to assign indexes and values to the
    # contents of any dictionary that ’ s already been defined.
    menus_specials = {}
    menus_specials["breakfast"] = "Canadian Ham"
    menus_specials["lunch"] = "tuna surprise"
    menus_specials["dinner"] = "cheeseburger deluxe"


    # When you ’ re using dictionaries, the indexes and values have special names. Index names in
    # dictionaries are called keys, and the values are called, well, values . To create a fully specified
    # (or you can think of it as a completely formed) dictionary — one with keys and values assigned at the
    # outset — you have to specify each key and its corresponding value, separated by a colon, between the
    # curly braces. For example, a different day ’ s specials could be defined all at once:
    menus_specials2 = {
        "breakfast" : "Sausage and eggs",
        "lunch" : "split pea soup and garlic bread",
        "dinner" : "2 hot dogs and onion rings"
    }

    print(menus_specials)
    print(menus_specials2)

    print("%s" % menus_specials["breakfast"])
    print("%s" % menus_specials["lunch"])
    print("%s" % menus_specials["dinner"])

    # If a key that is a string is accidentally not enclosed in quotes when you try to use it within square
    # brackets, Python will try to treat it as a name that should be dereferenced to find the key. In most
    # cases, this will raise an exception — a NameError — unless it happens to find a name that is the same
    # as the string, in which case you will probably get an IndexError from the dictionary instead!

    hungry = menus_specials.keys()
    print(list(hungry))
    starving = menus_specials2.values()
    print(list(starving))

    # Although you did not get an error, there is still a mistake in your code. When
    # you typed in the second key named “ breakfast ” , Python replaced the value in the first key with the
    # same name, and replaced the value of the second key with the same name.
    menu2 = {
        "breakfast": "spam",
        "breakfast": "ham",
        "dinner": "spam with a side of spam"
    }

    print(menu2)


if __name__ == "__main__":
    main()