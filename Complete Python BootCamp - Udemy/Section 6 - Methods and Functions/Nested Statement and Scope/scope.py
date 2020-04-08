# GLOBAL
name = 'This is a global string'

def greet():
    # ENCLOSING
    name = 'Sammy'

    def hello():
        # LOCAL
        name = 'This is local string'
        print('Hello ' + name)

    hello()

greet()