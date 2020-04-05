# Find out if the word "dog" is in the string
def dog_check(s):
    return 'dog' in s.lower()

print(dog_check('My dog ran away'))
print(dog_check('My Dog ran away'))
####################################################
# If word starts with a vowel, add 'ay' to the end
# If word does not start with a vowel, put first letter at the end, then add 'ay'
#       word -> ordway
#       apple -> appleay
def pig_latin(word):
    first_letter = word[0]

    if is_vowel(first_letter):
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'

    return pig_word

def is_vowel(letter):
    return letter.lower() in 'aeiou'

print(pig_latin('word'))
print(pig_latin('Apple'))
####################################################
def myfunc():
    print('Hello World')
####################################################
def myfunc(name):
    print('Hello {}'.format(name))
####################################################
def myfunc(greeting):
    if greeting:
        return 'Hello'
    else:
        return 'Goodbye'

def myfunc(greeting):
    return 'Hello' if greeting else 'Goodbye'
####################################################
def myfunc(x, y, z):
    return x if z else y
####################################################
def myfunc(a, b):
    return a + b
####################################################
def is_even(num):
    return num % 2 == 0
####################################################
def is_greater(c, d):
    return c > d
####################################################
