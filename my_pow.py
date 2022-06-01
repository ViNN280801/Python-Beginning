''' 
Documentation
Example for work with modules and variations of import
'''


def my_pow(param):
    ''' Returns powered number to 2.
    Gets 1 argument int or float types
    '''
    # Using double star ** to pow to 2nd degree
    return param**2


def print_my_pow(param):
    ''' 
    Printing result of 'my_pow()' function
    '''
    print(f'Result of squaring {param} is ' + str(my_pow(param)))

# Module may contain variables
var = 7
my_list = ['This', 'is', 'example', 5, 1, 9.04, 6]
