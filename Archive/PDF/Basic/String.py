# When you type a string into Python, you do so by preceding it with quotes. Whether these quotes are
# single ( ' ), double( '' ), or triple( " " " ) depends on what you are trying to accomplish. For the most part, you
# will use single quotes, because it requires less effort (you do not need to hold down the Shift key to
# create them). Note, however, that they are interchangeable with the double and even triple quotes.
def main():
    print("Hello World. You will never see this")
    print("This text really won't do anything")
    print("Hello, how are you?")
    print("1+1")
    print("@#@^#@@")

    print("This is a string with double quote")
    print('This is a string with single quote')
    print("""This is a string with tripe quotes""")

    print("I said, \"Don’t do it\"")

    print("John" + "Everyman")
    print("John" "Everyman")
    print("John " "Everyman")


if __name__ == "__main__":
    main()