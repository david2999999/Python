def main():
    # Tuples are immutable because they are supposed to be used for ordered groups of things that will not
    # be changed while you ’ re using them. Trying to change anything in them will cause Python to
    # complain with an error

    print("A %s %s %s %s" % ("string", "filled", "by a ", "tuple"))

    filler = ("string", "filled", "by a", "tuple")
    print(filler)
    print("A %s %s %s %s" % filler)

    a = ("first", "second", "third")
    print("The first element of the tuple is %s" % a[0])
    print("The second element of the tuple is %s" % a[1])
    print("The third element of the tuple is %s" % a[2])

    # A tuple keeps track of how many elements it contains, and it can tell you when you ask it by using the
    # built - in function len :
    print("%d" % len(a))

    print(a[len(a) - 1])
    b = (a, "b's second element")
    print(b)

    print("%s" % b[1])
    print("%s" % b[0][0])
    print("%s" % b[0][1])
    print("%s" % b[0][2])


    # An unrelated error will happen if you try to refer to an element in a tuple that doesn ’ t exist. If you try
    # to refer to the fourth element in a , you will get an error (remember that because tuples start counting
    # their elements at zero, the fourth element would be referenced using the number three):

    
if __name__ == "__main__":
    main()