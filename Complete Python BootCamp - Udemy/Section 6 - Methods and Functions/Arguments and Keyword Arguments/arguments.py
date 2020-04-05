def my_func(a, b):
    return sum((a, b)) * 0.05

print(my_func(40, 60))

# user can pass in as many arguments as we want and they will be treated as a single tuple
def my_func(*args):
    print(args)
    return sum(args) * 0.05

print(my_func(40, 60, 100))

def my_func(*args):
    for item in args:
        print(item)

my_func(40, 60, 100, 1, 34)
####################################################
def my_func(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("No such fruit here")

my_func(fruit='apple', veggie='lettuce')
####################################################
def my_func(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

my_func(10, 20, 30, fruit='orange', food='eggs', animal='dog')
