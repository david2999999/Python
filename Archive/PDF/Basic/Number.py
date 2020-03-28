# If a number ranged from – 2,147,483,648 to +2,147,483,647, it was deemed an integer. Anything larger was
# promoted to a long.
def main():
    print(type(1))  #<class 'int'>
    print(type(2000))
    print(type(9999999))

    # Although in everyday life 1.0 is the same number as 1, Python will automatically perceive 1.0 as
    # being a float; without the .0, the number 1 would be dealt with as the integer number one (which you
    # probably learned as a whole number in grade school), which is a different kind of number.
    print(type(1.0))  #<class 'float'>

    # You can see that when you try to mix imaginary numbers and other numbers, they are not added (or
    # subtracted, multiplied, or divided); they ’ re kept separate, in a way that creates a complex number.
    # Complex numbers have a real part and an imaginary part
    print(12j + 1)
    print(12j + 1.01)
    print(type(12j + 1))  #<class 'complex'>


if __name__ == "__main__":
    main()