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