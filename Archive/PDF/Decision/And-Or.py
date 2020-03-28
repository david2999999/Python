def main():
    # One kind of combination is the and operation, which says “ if the operation, value, or object on my left
    # evaluates to being True , move to my right and evaluate that. If it doesn ’ t evaluate to True , just stop and
    # say False — don ’ t do any more. ”
    print(True and True)
    print(False and True)
    print(True and False)
    print(False and False)

    # The other kind of combining operation is the or operator. Using the or tells Python to evaluate the
    # expression on the left , and if it is False , Python will evaluate the expression on the right. If it is True ,
    # Python will stop evaluation of any more expressions:
    print(True or True)
    print(True or False)
    print(False or True)
    print(False or False)


if __name__ == "__main__":
    main()