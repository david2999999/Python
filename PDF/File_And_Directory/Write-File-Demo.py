import os

def make_text_file():
    a = open('test.txt', "w")
    a.write("This is used to create a new text file")
    a.close()


def make_another_file():
    if os.path.isfile('test.txt'):
        print("you are trying to create a file that already exist")
    else:
        f = open('text.txt', "w")
        f.write("This is how you create a new text file")

make_text_file()
make_another_file()