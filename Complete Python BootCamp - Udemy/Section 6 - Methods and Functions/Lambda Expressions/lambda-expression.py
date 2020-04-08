my_nums = [1, 2, 3, 4, 5]
new_nums = list(map(lambda num: num ** 2, my_nums))
print(new_nums)

my_nums = [1, 2, 3, 4, 5, 6]
new_nums = list(filter(lambda num: num % 2 == 0, my_nums))
print(new_nums)

names = ['Andy', 'Eve', 'Sally']
first_letters = list(map(lambda name: name[0], names))
print(first_letters)

reversed_names = list(map(lambda name: name[::-1], names))
print(reversed_names)