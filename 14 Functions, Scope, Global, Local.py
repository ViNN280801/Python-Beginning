# Importing "math" module
from cmath import asin
import math

# 'count' is in global scope
count = 0
print('Before cycle count = ' + str(count))

# We can modify 'count' in local scope, for example, in "while" loop
while count != 10:
    count += 1
print('After cycle count = ' + str(count))

# Prints 'count' which is in global scope
def foo():
    some_new_variable = 'var'
    print('Print count from \'foo()\' function: count = ' + str(count))

# Calling "foo()" function
foo()

# If we try to execute following code, we would get an error, because 'some_new_variable' is in local scope of "foo()" function
# print(some_new_variable)
# Let's rewrite function "foo()" so that we can recive value from 'some_new_variable'

# Returns 'some_new_variable'
def foo():
    some_new_variable = 'var'
    print('Print count from \'foo()\' function: count = ' + str(count))
    return some_new_variable

# Now, we can assign returned value from "foo()" to a new variable
new_variable = foo()
print('Recieved value from "foo()" function: ' + new_variable)

some_value = 'b1117003'
print('\'some_value\' before modifying: ' + some_value)
# Prints modified 'some_value'
def print_some_value():
    # Modifying global variable 'some_value'
    global some_value
    some_value += ' + hello from print_some_value'
    print(some_value)

print('\'some_value\' after modifying: ')
print_some_value()

# It's recommended not to make global variables if it (your program) does not required it

# Let's consider how is the value passed between functions
# Initialize global variable
global_var = 'I am global'
print('\nglobal_var = ', global_var)

# Modifies 'global_var'
def foo_A():
    global global_var
    global_var = 'I was modified by "foo_A()" function'
    return foo_B(global_var)

# Prints splitted by spaces 'global_var' from "foo_A" function
def foo_B(param):
    splitted = param.split(' ')
    print('global_var = ' + str(splitted))

# Calling "foo_A()" function
foo_A()

var = 'global scope'
print('\'var\' = ' + var)

# So, let's Consider nested function
def original():
    var = 'original()\'s scope'
    def nested():
        var = 5.27
        var *= asin(0.625)
        print('Value from "nested()" function: ' + str(var))
    
    nested()
    print('Value from "original()" function: ' + str(var))

original()

print('\nAnother experience using \'nonlocal\' keyword: ')

var = 'global scope'
print('\'var\' = ' + var)
# Using 'nonlocal'
# So, let's Consider nested function
def original():
    var = 'original()\'s scope'
    def nested():
        # With using 'nonlocal' keyword we can modify 'var' from 92th line
        nonlocal var
        var = 'nested()\'s scope'
        print('Value from "nested()" function: ' + str(var))
    
    nested()
    print('Value from "original()" function: ' + str(var))

original()
