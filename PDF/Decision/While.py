def main():
    # The while ... : operation will first check for its test condition (the ... between the while and the : )
    # and if it ’ s True , it will evaluate the statements in its indented block a first time. After it reaches the end
    # of its indented block, which can include other indented blocks, it will once again evaluate its test
    # condition to see whether it is still True . If it is, it will repeat its actions again; however, if it is False ,
    # Python leaves the indented section and continues to evaluate the rest of the program after the while
    # ...: section. If names are used in the test condition, then between the first repetition and the next (and
    # the next, and so on), the value referred to by the name could have changed and on and on until there is
    # some reason to stop.
    i = 10
    while i > 0:
        print("Lift off in: ")
        print(i)
        i = i - 1


if __name__ == "__main__":
    main()