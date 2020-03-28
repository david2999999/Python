# Simple math looks about how you ’ d expect it to look. In addition to + and – , multiplication is
# performed by the asterisk, *, and division is performed by the forward slash, /.
def main():
    print(5 + 300)
    print(399 + 3020 + 1 + 3456)
    print(300 - 59994 + 20)
    print(4023 - 22.46)

    print(2000403030 * 392381727)
    print(2000403030 * 3923817273929)

    # Note that although Python can deal with some very large numbers, the results of some operations will
    # exceed what Python can accommodate. The shorthand for infinity, inf , is what Python will return
    # when a result is larger than what it can handle.
    print(2e304 * 3923817273929)
    print(2e34 * 3923817273929)

    # Before Python 3.1, division was a bit more interesting. Without help, Python would not coax one kind of
    # number into another through division. Only when you had at least one number that was a floating - point
    # component — that is, a period followed by a number — would floating - point answers be displayed. If
    # two numbers that were normal integers or longs (in either case, lacking a component that specifies a
    # value less than one, even if that is .0 ) were divided, the remainder would be discarded. This has since
    # been fixed, and now Python will still display the decimals, unless told otherwise.
    print(44/11)
    print(5.0/2.5)
    print(324/101)
    print(324.5/102.9)
    print(5/3)

    # In some instances, believe it or not, you still need only the
    # remainder portion of a division result. To find this part of the answer, you have to use the modulus
    # operator, which is the % .
    print(5 % 3)
    print(123 % 44)
    print(334 % 13)
    print(652 % 4)

    print(4023 - 22.4)


if __name__ == "__main__":
    main()