def main():
    # Sets are similar to dictionaries in Python, except that they consist of only keys with no associated values.
    # Essentially, they are a collection of data with no duplicates. They are very useful when it comes to
    # removing duplicate data from data collections.
    # Sets come in two types: mutable and immutable frozensets. The difference between the two is that with a
    # mutable set, you can add, remove, or change its elements, while the elements of an immutable frozenset
    # cannot be changed after they have been initially set.

    alphabet = ['a', 'b', 'b', 'c', 'a', 'd', 'e']
    print(alphabet)

    alph2 = set(alphabet)
    print(alph2)

    # The example works by taking the data collection, alphabet , and converting it to a set. Because sets do
    # not allow duplicate values, the extra ‘ b ’ and ‘ a ’ characters are removed. It was then assigned to
    # alph2 , and printed to show the results.


if __name__ == "__main__":
    main()