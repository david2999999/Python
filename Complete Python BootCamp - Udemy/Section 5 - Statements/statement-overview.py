# Use 'for', .split(), and 'if' to create a statement that will print out words
# that start with 's'
st = 'Sam Print only the words that start with s in this sentence'
for word in st.split():
    if word[0].lower() == 's':
        print(word)

# Use range() to print all the even numbers from 0 to 10
for num in range(0, 11, 2):
    if num % 2 == 0:
        print(num)

# Use a List Comprehension to create a list of all numbers between 1 and 50 that are
# divisible by 3
my_list = [x for x in range(1, 50) if x % 3 == 0]
print(my_list)

# Go through the string below and if the length of a word is even, print "even"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print(word)

# Write a program that prints the integers from 1 to 100
# But for multiples of three print "Fizz" instead of the number
# For multiples of five, print "Buzz"
# For numbers which are multiples of both three and five print "FizzBuzz"
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('FizzBuzz')
    elif num % 3 == 0:
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(num)

# Use List Comprehensions to create a list of the first letters of every word
# in the string below
st = 'Create a list of the first letters of every word in this string'
my_list = [word[0] for word in st.split()]
print(my_list)