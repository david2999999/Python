def main():
    # Suppose you have two lists that you want to join together. You haven ’ t been shown a purposely built
    # way to do that yet. You can ’ t use append to take one sequence and add it to another. Instead, you will
    # find that you have layered a sequence into your list:
    living_room = ("rug", "table", "chair", "TV", "dustbin", "shelf")

    apartment = []
    apartment.append(living_room)

    print(apartment)

    # To copy all of the elements of a sequence, instead of using append , you can use the extend method of
    # lists and tuples, which takes each element of the sequence you give it and inserts those elements into the
    # list from which it is called:
    apartment2 = []
    apartment2.extend(living_room)
    print(apartment2)

if __name__ == "__main__":
    main()