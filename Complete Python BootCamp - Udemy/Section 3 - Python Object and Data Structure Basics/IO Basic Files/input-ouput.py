with open('Test File.txt') as my_file:
    print(my_file.read())

    my_file.seek(0)
    print(my_file.read())

    my_file.seek(0)
    print(my_file.readlines()) # ['This a Test File.\n', 'This a Test File Line 2.\n', 'This a Test File Line 3.']

with open('Test File.txt', mode='r') as my_file:
    contents = my_file.read()
    print(contents)

with open('Test File.txt', mode='a') as append_file:
    append_file.write('\nAdding new Line')

with open('New File.txt', mode='w') as append_file:
    append_file.write('Created New file')


# Different Modes
    # mode = 'r' is read only
    # mode = 'w' is write only
    # mode = 'a' is append only
    # mode = 'r+' is reading and writing
    # mode = 'w+' is writing and reading