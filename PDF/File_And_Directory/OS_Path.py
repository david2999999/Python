import os

def using_os_path():
    # prints ‘snakes\\Python’ on window
    # prints ‘snakes/Python’ on linux
    print(os.path.join("snakes", "Python"))


def using_path_split():
    parent_path, name = os.path.split("C:\\Program Files\\Python30\\Lib")
    print(parent_path)
    print(name)

using_os_path()
using_path_split()