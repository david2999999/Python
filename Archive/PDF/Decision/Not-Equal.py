def main():
    print(3 == 3)
    print(3 != 3)
    print(5 != 4)

    tuesday_breakfast_sold = {
        "pancakes": 10,
        "french toast": 4,
        "bagels": 32,
        "omelet": 12,
        "eggs and sausages": 13
    }

    wednesday_breakfast_sold = {
        "pancakes": 8,
        "french toast": 4,
        "bagels": 12,
        "omelet": 10,
        "eggs and sausages": 13
    }

    thursday_breakfast_sold = {
        "pancakes": 10,
        "french toast": 4,
        "bagels": 32,
        "omelet": 12,
        "eggs and sausages": 13
    }

    # Every pair of numbers that would generate a True result when they ’ re compared using the == will
    # now generate a False , and any two numbers that would have generated a False when compared
    # using == will now result in True .
    print(tuesday_breakfast_sold != wednesday_breakfast_sold)
    print(tuesday_breakfast_sold != thursday_breakfast_sold)


if __name__ == "__main__":
    main()