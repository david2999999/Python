def read_file():
    a = open("test.txt", "r")
    print(a.readline())
    a.close()

def read_file2():
    f = open("test.txt", "r")
    text = f.read()
    print(text)
    f.close()

def print_line_length():
    a = open("test.txt", "r")
    text = a.readlines()

    for line in text:
        print(len(line))

    a.close()

read_file()
read_file2()
print_line_length()