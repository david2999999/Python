# Build-in objects in Python have a variety of methods
my_list = [1, 2, 3]
my_list.append(4) # method in list
my_list.pop() # method in list

def name_function():
    """
    DOCSTRING: Information about the function
    Input: No input..
    Output: Hello ...
    """
    print('hello')

help(name_function)
name_function()
####################################################
def say_hello(name='NAME'):
    return 'Hello ' + name

result = say_hello()
print(result)
result = say_hello('Sally')
print(result)
####################################################
def add(n1, n2):
    return n1 + n2

print(add(20, 30))
