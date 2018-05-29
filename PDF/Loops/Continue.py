# There is one other commonly used feature for loops: the continue statement. When continue is
# used, you ’ re telling Python that you do not want the loop to be terminated, but that you want to skip
# the rest of the current repetition of the loop, and if you ’ re in a for ... in ...: loop, re - evaluate the
# conditions and the list for the next round.
def main():
    for food in ("pate", "cheese", "rotten apple", "crackers", "whip cream", "tomato soup"):
        if food[0:6] == "rotten":
            continue

        print("you can eat %s" % food)


    # Because you ’ ve used an if ... : test to determine whether the first part of each item in the food list
    # contains the string “ rotten ” , the “ rotten apples ” element will be skipped by the continue ,
    # whereas everything else is printed as safe to eat.

if __name__ == "__main__":
    main()