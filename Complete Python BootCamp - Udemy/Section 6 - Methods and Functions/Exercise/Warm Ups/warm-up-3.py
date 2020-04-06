# Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20

# def makes_twenty(n1, n2):
#     return True if n1 + n2 == 20 else (n1 == 20 or n2 == 20)

def makes_twenty(n1, n2):
    return n1 + n2 == 20 or n1 == 20 or n2 == 20

print(makes_twenty(20, 10))
print(makes_twenty(12, 8))
print(makes_twenty(2, 3))
print(makes_twenty(10, 10))