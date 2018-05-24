def main():
    # All of the sequence types provide you with some shortcuts to make their use more convenient. You often
    # need to know the contents of the final element of a sequence, and you can get that information in two
    # ways. One way is to get the number of elements in the list and then use that number to directly access
    # the value there:
    last_names = ["Douglass", "Jefferson", "Williams", "Frank", "Thomas"]
    print(len(last_names))

    last_element = len(last_names) - 1
    print("%s" % last_names[last_element])

    #     However, that method takes two steps; and as a programmer, typing it repeatedly in a program can be
    # time - consuming. Fortunately, Python provides a shortcut that enables you to access the last element of a
    # sequence by using the number – 1, and the next - to - last element with – 2, letting you reverse the order of
    # the list by using negative numbers from – 1 to the number that is the negative length of the list (– 5 in the
    # case of the last_names list).
    print("%s" % last_names[-1])
    print("%s" % last_names[-2])
    print("%s" % last_names[-3])


if __name__ == "__main__":
    main()