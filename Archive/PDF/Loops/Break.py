# Infinite loops can be exited by using the break statement.
def main():
    age = 0

    while True:
        how_old = input("Enter your age: ")
        if how_old == "no":
            print("Don't be ashamed of your age!")
            break

        num = int(how_old)
        age = age + num

        print("Your age is " + str(age))
        print("That is old!")

    # In the preceding program, While , as you may recall, is always equal to True ; therefore, the statement
    # while True will always loop if left to its own devices. To solve this, you prompt the user for some info;
    # in this case, their age. So long as they enter in a number, the program will add it to their age, giving them
    # a total age and making it appear that they are getting older (unless they are savvy and enter in a negative
    # number, in which case they will get younger!). If they enter only numbers, the program will run forever.
    # However, if they ever enter in the string, No , the program will print Don ’ t be ashamed of your age!
    # and break out of the loop.
if __name__ == "__main__":
    main()