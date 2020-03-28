def main():
    breakfast = ["coffee", "tea", "toast", "egg"]

    count = 0
    print("Today's breakfast is %s" % (breakfast[count]))

    count = 1
    print("Today's breakfast is %s" % (breakfast[count]))

    count = 2
    print("Today's breakfast is %s" % (breakfast[count]))

    count = 3
    print("Today's breakfast is %s" % (breakfast[count]))

    # The primary difference in using a list versus using a tuple is that a list can be modified after it has
    # been created. The list can be changed at any time:
    breakfast[count] = "sausages"
    print("Today's breakfast after the change is %s" % breakfast[count])


    # You don ’ t just have to change elements that already exist in the list, you can also add elements to the
    # list as you need them. You can add elements at the end by using the append method that is built in to
    # the list type. Using append enables you to append exactly one item to the end of a list:
    breakfast.append("waffles")
    count = 4
    print("Today's breakfast after the addition is %s" % breakfast[count])

    # If you want to add more than one item to the end of a list — for instance, the contents of a tuple or of
    # another list — you can use the extend method to append the contents of a list all at once. The list isn ’ t
    # included as one item in one slot; each element is copied from one list to the other:
    breakfast.extend(["juice", "decaf", "oatmeal"])
    print(breakfast)

if __name__ == "__main__":
    main()