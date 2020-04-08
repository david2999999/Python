def square(num):
    return num ** 2

my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

new_list = list(map(square, my_nums))
print(new_list)

def splicer(my_string):
    if len(my_string) % 2 == 0:
        return 'EVEN'
    else:
        return my_string[0]

names = ['Andy', 'Eve', 'Sally']
print(list(map(splicer, names)))