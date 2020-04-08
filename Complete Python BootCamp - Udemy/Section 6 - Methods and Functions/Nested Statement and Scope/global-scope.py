x = 50

def func():
    global x
    print(f'X is {x}')

    x = 200 # local reassignment on a global variable
    print(f'Reassigned global x locally to {x}')

func()
print(x)