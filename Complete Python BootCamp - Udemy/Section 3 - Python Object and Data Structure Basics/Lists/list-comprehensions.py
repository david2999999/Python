# List Comprehensions are a unique way of quickly creating a list
# If you find yourself using a 'for' loop along with .append() to create a list
#   List comprehensions are a good alternative
my_list = []

my_string = 'hello'
for letter in my_string:
    my_list.append(letter)
print(my_list)

my_list = [letter for letter in my_string]
print(my_list)

my_list = [x for x in 'word']
print(my_list)

my_list = [num for num in range(0, 11)]
print(my_list)

my_list = [num ** 2 for num in range(0, 11)]
print(my_list)

my_list = [x for x in range(0, 11) if x % 2 == 0]
print(my_list)

celcius = [0, 10, 20, 34.5]
fahrenheit = [((9/5) * temp + 32) for temp in celcius]
print(fahrenheit)

results = [x if x % 2 == 0 else 'ODD' for x in range(0, 11)]
print(results)

my_list = []
for x in [2, 4, 6]:
    for y in [100, 200, 300]:
        my_list.append(x * y)
print(my_list)

my_list = [x * y for x in [2, 4, 5] for y in [1, 10, 1000]]
print(my_list)