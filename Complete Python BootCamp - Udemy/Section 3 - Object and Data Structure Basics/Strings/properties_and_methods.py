name = "Sam"
# name[0] = 'P' - TypeError: 'str' object does not support item assignment

last_letters = name[1:]
print(last_letters)

last_letters = 'P' + last_letters
print(last_letters)

hello_world = "Hello World"
hello_world = hello_world + " it is beautiful outside"
print(hello_world)

hello_world += hello_world
print(hello_world)

letter = 'z'
print(letter * 10)

x = "Hello World"
print(x.upper())
print(x.lower())
print(x.split()) # splits default on white space

x = 'this is a string'
print(x.split('i'))