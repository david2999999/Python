def main():
    fridge_content = {"egg" : 8, "mushrooom": 20, "pepper" : 3, "cheese" : 2, "tomato" : 4, "milk" : 13}

    # Because there is no key in the fridge_contents dictionary for “ orange juice ” , a KeyError is
    # raised by Python to let you know that no such key is available. In addition, you specified the name
    # error, which Python will use to reference a string that contains any information about the error that
    # Python can offer. We achieve this by using the as keyword to assign the value of the KeyError to error.
    # In this case, the string relates to the key that was requested but not present in the fridge_contents
    # dictionary (which is, again, “ orange juice ” ).
    try:
        if fridge_content["orange juice"] > 3:
            print("Sure lets have some juice!")
    except KeyError as error:
        print("Aww, there is %s juice. Let's go shoppping" % error)

    # There may be times when you handle more than one type of error in exactly the same way; and in
    # those cases, you can use a tuple with all of those exception types described:
    try:
        if fridge_content["orange juice"] > 3:
            print("Sure lets have some juice!")
    except (KeyError, TypeError) as error:
        print("Aww, there is %s juice. Let's go shoppping" % error)


    # If you have an exception that you need to handle, but you want to handle it by not doing anything (for
    # cases in which failure isn ’ t actually a big deal), Python will let you skip that case by using the special
    # word pass
    try:
        if fridge_content["orange juice"] > 3:
            print("Sure lets have some juice!")
    except KeyError as error:
        print("Aww, there is %s juice. Let's go shoppping" % error)
    except TypeError:
        pass

if __name__ == "__main__":
    main()