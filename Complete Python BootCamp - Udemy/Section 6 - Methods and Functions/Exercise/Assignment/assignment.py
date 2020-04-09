# Write a function that computes the volume of a sphere given its radius
def volume(rad):
    return (4.0 / 3) * 3.14 * (rad ** 3)

# Write a function that checks whether a number is in a given range (inclusive
# of high and low)
def ran_check(num, low, high):
    if num in range(low, high + 1):
        print("%s is in the range" % str(num))
    else:
        print("The number is outside the range")

# Write a function that accepts a string and calculate the number of upper case
# letters and lower case letters
def up_low(s):
    d = {
        "upper": 0,
        "lower": 0
    }

    for c in s:
        if c.isupper():
            d["upper"] += 1
        elif c.islower():
            d["lower"] += 1
        else:
            pass

    print("Original String : ", s)
    print("No. of Upper case characters: ", d["upper"])
    print("No. of Lower case characters: ", d["lower"])

up_low('Hello Mr.Rogets, how are you this fine Tuesday?')

# Write a python function that takes a list and returns a new list with
# unique elements of the first list
def unique_list(sample_list):
    unique_list = []
    for a in sample_list:
        if a not in unique_list:
            unique_list.append(a)
    return unique_list

# Wrie a python function to multiple all the numbers in a list
def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total

# Write a function that checks whether a passed string is a palindrome
def palindrome(s):
    return s == s[::-1]

# Write a function that check whether a string is pangram or not
import string
def is_pangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())
