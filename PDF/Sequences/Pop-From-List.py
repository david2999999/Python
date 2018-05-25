def main():
    # You need to tell pop which element it is acting on. If you tell it to work on element 0, it will pop the
    # first item in its list, passing pop a parameter of 1 will tell it to use the item at position 1 (the second
    # element in the list), and so on. The element pop acts on is the same number that you ’ d use to access
    # the list ’ s elements using square brackets (remember that the first value in a list is 0):
    todays_temperature = [23, 32, 33, 31]
    todays_temperature.append(29)
    print(todays_temperature)

    morning = todays_temperature.pop(0)
    print("This morning's temperature was %.02f" % morning)

    late_morning = todays_temperature.pop(0)
    print("Todays late morning's temperature was %.02f" % late_morning)

    noon = todays_temperature.pop(0)
    print("Today's noon temperature was %.0f" % noon)

    print(todays_temperature)

    #     When a value is popped, if the action is on the right - hand side of an equals sign, you can assign the
    # element that was removed to a value on the left - hand side, or just use that value in cases where it
    # would be appropriate. If you don ’ t assign the popped value or otherwise use it, it will be discarded
    # from the list.


if __name__ == "__main__":
    main()