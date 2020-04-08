# Write a function that takes in a list of integers and returns True if it contains
# 007 in order
def spy_game(nums):
    code = [0, 0, 7]

    for num in nums:
        if num == code[0]:
            code.pop(0)

        if len(code) == 0:
            return True

    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7]))
print(spy_game([1,7,2,0,5,4]))