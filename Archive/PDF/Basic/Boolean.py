def main():
    # True and False are special representations of the numbers 1 and 0. This prevents a lot of the confusion
    # that is common in other programming languages where the truth value of a statement is arbitrary. For
    # instance, in a UNIX shell (shell is both how you interact with the system, as well as a programming
    # language), 0 is true and anything else is false. With C and Perl, 0 is false and anything else is true.
    # However, in all of these cases, there are no built - in names to distinguish these values. Python makes this
    # easier by explicitly naming the values
    print(True)
    print(False)
    print(True == 1)
    print(True == 0)
    print(False == 1)
    print(False == 0)
    print(False > 0)
    print(False < 1)



if __name__ == "__main__":
    main()