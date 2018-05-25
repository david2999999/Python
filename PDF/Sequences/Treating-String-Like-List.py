def main():
    last_names = ["Douglass", "Jefferson", "Williams", "Frank", "Thomas", "Tim"]
    print("%s" % last_names[0])
    print("%s" % last_names[0][1])
    print("%s" % last_names[1])
    print("%s" % last_names[1][2])
    print("%s" % last_names[2])
    print("%s" % last_names[2][0])

    # For example, you can use the letter positioning of strings to arrange them into groups in a dictionary
    # based on the first letter of the last name. You don ’ t need to do anything complicated; you can just check
    # to see which letter the string containing the name starts with and file it under that:
    by_letter = {}
    by_letter[last_names[0][0]] = last_names[0]
    by_letter[last_names[1][0]] = last_names[1]
    by_letter[last_names[2][0]] = last_names[2]
    by_letter[last_names[3][0]] = last_names[3]
    by_letter[last_names[4][0]] = last_names[4]
    print(by_letter)

    # The by_letter dictionary will, thanks to string slicing, only contain the first letter from each of the last
    # names. Therefore, by_letter is a dictionary indexed by the first letter of each last name. You could
    # also make each key in by_letter reference a list instead and use the append method of that list to create
    # a list of names beginning with that letter (if, of course, you wanted to have a dictionary that indexed a
    # larger group of names, where each one did not begin with a different letter).


if __name__ == "__main__":
    main()