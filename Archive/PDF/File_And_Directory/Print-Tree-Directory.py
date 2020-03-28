import os

def print_tree(dir_path):
    for name in os.listdir(dir_path):
        full_path = os.path.join(dir_path, name)
        print(name)
        print(full_path)

        if os.path.isdir(full_path):
            print_tree(full_path)

print_tree("C:\\Users\\david2999999\\Desktop\\Python\\PDF")