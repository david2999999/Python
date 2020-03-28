# Both while ... : and for ... in ... : loops can have an else: statement at the end of the loop,
# but it will be run only if the loop doesn ’ t end due to a break statement. In this case, else: could be
# better named something like done or on_completion , but else: is a convenient name because you ’ ve
# already seen it, and it ’ s not hard to remember.
def main():
    for food in ("pate", "cheese", "cracker", "yogurt") :
        if food == "yogurt":
            break
    else:
        print("There is no Yogurt")


    # Only this for statement will print "there is no yogurt"
    for food in ("pate", "cheese", "crackers"):
        if food == "yogurt":
            break
    else:
        print("There is no yogurt")


if __name__ == "__main__":
    main()