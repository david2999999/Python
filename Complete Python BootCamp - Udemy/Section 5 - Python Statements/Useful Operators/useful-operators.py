my_list = [1, 2, 3]
for num in range(0, 11, 2):
    print(num)

print(list(range(0, 11, 2)))

index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

word = 'abcdef'
for index, letter in enumerate(word):
    print(f'{index} {letter}')

my_list1 = [1, 2, 3]
my_list2 = ['a', 'b', 'c']

for item in zip(my_list1, my_list2):
    print(item)

print(list(zip(my_list1, my_list2)))

print('x' in [1, 2, 3])
print(2 in [1, 2, 3])
print('a' in 'a world')
print('myKey' in {'myKey':345})
print(345 in {'myKey':345}.values())

my_list = [10, 20, 30, 40, 100]
print(min(my_list))
print(max(my_list))

from random import shuffle
my_list = [1,2,3,4,5,6,7,8,9,10]
shuffle(my_list)
print(my_list)

from random import randint
print(randint(0, 100))

result = input('What is your name? ')
print(f'name = {result}')

result = input('What is your Favorite Number? ')
print(f'name = {result}')
float(result)
int(result)