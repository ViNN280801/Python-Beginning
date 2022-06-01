# Decorator is the function that allows to wrap another function in it's code
# Decorators designed for adding functionality to old funcitons
# in order not to interfere with the code and not to violate the structure of program

from subprocess import call


def make_decor(name):
    # Nested 'wrapper()' funciton
    def wrapper():
        print('Decorator code')
        name()
        print('Decorator code')
    return wrapper

# '@' symbol points on decorator
# make() = make_decor(make)


@make_decor
def make():
    enter = input('Enter something: ')
    print(enter)


# Calling 'make()' function
make()

# Let's view error handler in decorator
# For do this, we need to create a few functions which can calls error, in our exaple trying convert 'str' type to 'float' type


def decor(function_name):
    def wrapper():
        while True:
            try:
                call_func = function_name()
                break
            except:
                print('Incorrect data input. Try again')
        return call_func
    return wrapper


@decor
def make():
    enter = float(input('Enter a number: '))
    return enter


@decor
def make_again():
    enter = float(input('Enter a number again please: '))
    return enter


make()
make_again()
