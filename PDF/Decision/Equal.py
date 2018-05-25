def main():
    # You can also use the double equals to test whether strings have the same contents, and you can even
    # restrict this test to ranges within the strings (remember from the last chapter that slices create copies of
    # the part of the strings they reference, so you ’ re really comparing two strings that represent just the
    # range that a slice covers):
    a = "Macktintosh apples"
    b = "Black Berries"
    c = "Golden Delicious apples"
    print(a == b)
    print(b == c)
    print(a[-len("apple"):-1] == c [-len("apple"):-1])

    #   Sequences can be compared in Python with the double equals as well. Python considers two
    # sequences to be equal when every element in the same position is the same in each list. Therefore, if
    # you have three items each in two sequences and they contain the same data but in a different order,
    # they are not equal:
    apples = ["Mactintosh", "Golden Delicious", "Fuji", "Mitsu"]
    apple_trees = ["Golden Delicious", "Fuji", "Mitsu", "Mactintosh"]
    print(apple_trees == apples)
    apple_trees2 = ["Mactintosh", "Golden Delicious", "Fuji", "Mitsu"];
    print(apple_trees2 == apples)

    #     In addition, dictionaries can be compared. Like lists, every key and value (paired, together) in one
    # dictionary has to have a key and value in the other dictionary in which the key in the first is equal to
    # the key in the second, and the value in the first is equal to the value in the second:
    tuesday_breakfast_sold = {
        "pancakes" : 10,
        "french toast" : 4,
        "bagels" : 32,
        "omelet" : 12,
        "eggs and sausages" : 13
    }

    wednesday_breakfast_sold = {
        "pancakes": 8,
        "french toast": 4,
        "bagels": 12,
        "omelet": 10,
        "eggs and sausages": 13
    }

    print(tuesday_breakfast_sold == wednesday_breakfast_sold)

    thursday_breakfast_sold = {
        "pancakes": 10,
        "french toast": 4,
        "bagels": 32,
        "omelet": 12,
        "eggs and sausages": 13
    }

    print(tuesday_breakfast_sold == thursday_breakfast_sold)

    
if __name__ == "__main__":
    main()