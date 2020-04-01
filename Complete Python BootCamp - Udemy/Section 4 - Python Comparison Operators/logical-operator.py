# We can use logical operators to combine comparisons
    # and, or, not

# 'and' keyword needs both conditions to be true in order for the result to be true
print(1 < 2 and 2 < 3) # True
print('h' == 'h' and 2 == 2) # True

# 'or' keyword needs at least one condition to be true in order for the result to be true
print(1 == 1 or 2 == 2) # True
print(1 == 1 or 2 == 3) # True
print(100 == 1 or 2 == 200) # False

# 'not' keyword returns the opposite boolean
print(not 1 == 1) # false
print(not 400 > 5000) # True