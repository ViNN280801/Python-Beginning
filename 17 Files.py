# Importing 'os' library
import os

# Initializing empty list
list_paths = []

# Splitting returned list from 'os.walk()' to 3 variables
for address, dirs, files in os.walk(input('Enter path: ')):
    # Iteration by files in 'files' list
    for file in files:
        # Joining by "address + file" path to create full path
        full_path = os.path.join(address, file)
        # Appending to list of paths full path of certain file
        list_paths.append(full_path)

# 'r' - open for read (by default)
# 't' - open in text mode (by default)
# 'w' - open in write mode, file content removes, if there is no such file -> creates it
# 'a' - open in append mode to the end of file, if there is no such file -> creates it
# 'b' - open file in binary mode
# '+' - open for read and write 'r+', 'w+', 'a+'

# Creating file using 'open()' function
# Always when you openning file, you have to close it in the end of work with it
print('Opening file my_file.txt ...')
my_file = open('my_file.txt', 'w+')
# Writing data to file
print('Writing data to file ...')
my_file.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. In a neque velit.')
# Closing file after work with it
my_file.close()
print('my_file.txt has been closed')

# Opening file in read mode
print('\nOpening file my_file.txt ...')
my_file = open('my_file.txt', 'r')
# Reading data in variable from file using 'read()' method
data_from_my_file = my_file.read()
print('Read data from file: ' + data_from_my_file)
# Closing file after reading data from it
my_file.close()
print('my_file.txt has been closed')

# Opening file in write mode
print('\nOpening file paths_file.txt ...')
paths_file = open('paths_file.txt', 'w')
# Iteration by paths with 'for' loop
# Writing each path to file
print('Writing paths to that file ...')
for path in list_paths:
    paths_file.write(str(path) + '\n')
# Closing file
paths_file.close()
print('paths_file.txt has been closed')

# Opening file in read mode
print('\nOpening file paths_file.txt ...')
paths_file = open('paths_file.txt', 'r')
# Read 1st line from file and write result in 'str_path' variable
str_path = paths_file.readline()
print('Read data from 1st line of file paths_file.txt:\n' + str(str_path))
# Iteration by paths with 'for' loop
# Writing each path to file
print('Reading lines from that file ...')
# Read all lines as list from file in one variable
str_paths = paths_file.readlines()
print('All paths in one variable:\n' + str(str_paths))
# Closing file
paths_file.close()
print('paths_file.txt has been closed')

# Opening one executive file to read, another to write (we will wite data from original file to copy)
exe_file = open('samples1.exe', 'rb')
exe_file_copy = open('samples1(copy).exe', 'wb')

print('\nRewriting executive file into copy ...')
# If file size is more than 512 Mb (so as not to read it all in RAM)
while True:
    # Reading 1 Mb -> 1024 Kb -> 1024 * 1024 byte -> 1 048 576 byte
    var = exe_file.read(1024 * 1024)
    # Using '__sizeof()__' function to view how much RAM does the object 'var' take up
    print('\'var\' taking up ' + str(var.__sizeof__()) + ' bytes')
    # For example, if var = 33 bytes, loop will be breaked
    if var.__sizeof__() == 33:
        break
    # Writing data from 'var' to copy of executive file
    exe_file_copy.write(var)

# Closing files after work with them
exe_file.close()
exe_file_copy.close()

# Opening file in utf-8 encoding (3rd parameter) of function open()
print('\nOpening encoding_file.txt: ')
encoding_file = open('encoding_file.txt', 'w', encoding = 'utf-8')
# Printing 'encoding_file' data
print(encoding_file)
# Closing file after work
encoding_file.close()

print('\nDo you want to delete all created and used files by this program? ')
# Using infinite loop for handling incorrect input data
while True:
    # Initializing variable responsible to delete files
    is_delete = input('y/n: ')
    if is_delete == 'y':
        # Using 'remove()' method of 'os' module to remove files
        os.remove('my_file.txt')
        os.remove('paths_file.txt')
        os.remove('samples1(copy).exe')
        os.remove('encoding_file.txt')
        
        while True:
            print('Do you want to delete samples1.exe? ')
            is_delete = input('y/n: ')
            if is_delete == 'y':
                os.remove('samples1.exe')
                print('File samples1.exe have been deleted')
                break
            elif is_delete == 'n':
                print('File samples1.exe haven\'t been deleted')
                break
            else:
                print('Entered choose is invalid. Try again: ')

        print('All choosen files which were created or used by this program have been deleted')
        break
    elif is_delete == 'n':
        print('Files haven\'t been deleted')
        break
    else:
        print('Entered choose is invalid. Try again: ')
