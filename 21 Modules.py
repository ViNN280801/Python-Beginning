# Importing 'my_pow.py' different ways

# Importing module using 'import' keyword
import my_pow

# Importing module using 'from' and 'import' keywords
# Following commented line importing all contains from my_pow

# from my_pow import *

# Importing module using 'from' and 'import' keywords
# Following commented line importing only 'print_my_pow()' function

# from my_pow import print_my_pow

# 'dir()' function returns list of all attributes of module
print('dir(): ' + str(dir()))
# Printing list of attributes of 'my_pow'
print('\nmy_pow contains: ' + str(dir(my_pow)))
# 'help()' calls the built-in Python help system
# print(help(my_pow))

# Using 'my_pow'
print('\n3.91^2 = ' + str(my_pow.my_pow(3.91)))
my_pow.print_my_pow(3.91)
