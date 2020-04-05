def myfunc(*args):
    return sum(args)
####################################################
def myfunc(*args):
    return [num for num in args if num % 2 == 0]
####################################################
def myfunc(word):
    result = []

    for index, letter in enumerate(word):
        if index % 2 == 0:
            result.append(letter.upper())
        else:
            result.append(letter.lower())

    return ''.join(result)