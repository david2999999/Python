# lesser of two evens: write a function that returns the lesser of the two given numbers
# if both numbers are even, but return the greater if one or both numbers are odd
def lesser_of_two_events(a, b):
    if is_even(a) and is_even(b):
        return a if a < b else b
    else:
        return a if a > b else b

def lesser_of_two_events2(a, b):
    if is_even(a) and is_even(b):
        return min(a, b)
    else:
        return max(a, b)

def is_even(num):
    return num % 2 == 0

print(lesser_of_two_events(2, 4))
print(lesser_of_two_events(7, 5))

print(lesser_of_two_events2(2, 4))
print(lesser_of_two_events2(7, 5))