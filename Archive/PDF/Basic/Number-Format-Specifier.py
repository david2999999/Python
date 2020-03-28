def main():
    print("$%.02f" % 30.0)
    print("$%.03f" % 30.00123)
    print("%.03f" % 30.1777)
    print("%.03f, %f %d" % (30.1113, 12, 13))

    print('Octal uses the letter "o" lowercase. %d %o' % (10, 10))
    print('Hex uses the letter "x" or "X. %d %x %X' % (10, 10, 10))


if __name__ == "__main__":
    main()