# A try: statement sets up a situation in which an except: statement can follow it. Each except:
# statement handles the error, which is formally named an exception that was just raised when Python
# evaluated the code within the try: statement instead of failing. To start with, use except: to handle
# one type of error — for instance, the KeyError that you get when trying to check the fridge.
def main():
    fridge_content = {"egg" : 8, "mushrooom": 20, "pepper" : 3, "cheese" : 2, "tomato" : 4, "milk" : 13}

    try:
        if fridge_content["orange juice"] > 3:
            print("Sure lets have some juice!")
    except KeyError:
        print("Aww, there is no juice. Let's go shoppping")


if __name__ == "__main__":
    main()