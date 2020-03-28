import os

def make_text_file():
    a = open('test.txt', "w")
    a.write("This is used to create\n a new text file\n random text here \n more text")
    a.close()


def make_another_file():
    if os.path.isfile('test.txt'):
        print("you are trying to create a file that already exist")
    else:
        f = open('text.txt', "w")
        f.write("This is how you create a new text file")

def add_some_text():
    a = open('test.txt', "a")
    a.write("Additional text appended")

make_text_file()
make_another_file()
add_some_text()