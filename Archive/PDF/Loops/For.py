def main():
    # Doing this the other way, with the for ... in ... : form of repetition, is, as shown before, very
    # similar to the while ... : form, but it saves you a couple of steps. In the first part, the for ... , you
    # once more assign a variable name (again you use i , a common practice, because it is short for index).
    # In the second part, the in ... : part, you provide a sequence, such as a list, tuple, or in this course, a
    # range , which takes each element and assigns the value of the element to the name you provided in the
    # first part:
    for i in range(10, 0, -1):
        print("T-minus: ")
        print(i)

    for i in range(10):
        print(i)

if __name__ == "__main__":
    main()