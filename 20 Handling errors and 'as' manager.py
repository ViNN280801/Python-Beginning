# Importing 'os' module
import os

# Handling number errors with 'try' and 'except' operators
# Using infinite loop to handling error
while True:
    try:
        enter = float(input('Enter a number: '))
        print(f'100/{enter} = ' + str(100/enter))
        break
    except:
        print('Incorrect data input. Try again')
    # Finally executing always
    finally:
        print('Hello from \'finally\'')

# Handling file error with 'try' and 'except' operators
# Using infinite loop to handling error
while True:
    try:
        filename = input('Enter name of file to read: ')
        file = open(f'{filename}', 'r')
        print('Reading data from file...')
        data = file.read()
        file.close()
        break
    except:
        print('There is no such file. Try again')

print('Read data from file:\n' + data)

# Typical work with file
# Opening or create file (if it doesn't exist)
file = open('text.txt', 'w')
# Writing data to file
file.write('Execution speed. Gumbo gains some of this by virtue of being written in C,' +
           'but it is not an important consideration for the intended use-case, and was not a major design factor.\n')
# Closing file
file.close()

# Work with file using 'with'
# Opening file
with open('text.txt', 'w') as file:
    # Writing data to file
    file.write('Execution speed. Gumbo gains some of this by virtue of being written in C,' +
               'but it is not an important consideration for the intended use-case, and was not a major design factor.\n')
    # Generating error
    10 / 0
    # There we don't need to write 'file.close()', because operator 'with' closed it when it's work was ended
    # And file will safely closed in any case (even if we occur error)
    # 'with' doesn't handling errors

print('Do you want to delete file which uses in working of this program? ')
while True:
    is_delete = input('y/n: ')
    if is_delete == 'Y' or is_delete == 'y':
        # Deleting file
        os.remove('text.txt')
        print('File text.txt has been removed')
        break
    elif is_delete == 'N' or is_delete == 'n':
        print('File text.txt hasn\'t been removed')
        # Breaking the loop
        break
    else:
        print('Incorrect data input. Try again')
