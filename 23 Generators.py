# Importing 'os' module
from encodings import utf_8
import os
from stat import filemode

''' Generators of list, sets and dictionaries '''

my_list = [1, 8, -4, 13, 9, 5, -136, 74, -9, 56, -91, 34, 82, 0, -3, -7]
print('my_list: ' + str(my_list))

# Typical way to create new list with some changes
new_list = []
for elem in my_list:
    new_list.append(elem * 2)
print('new_list: ' + str(new_list))

# Minimal syntax for generator of list
# This way is quicker than previous
new_list_2 = [elem * 2 for elem in my_list]
print('new_list_2: ' + str(new_list_2))

# Generator for set
my_set = {elem * 0.5 for elem in my_list}
print('my_set: ' + str(my_set))

# Generator for dictionary
my_dict = {elem: str(elem) + 'ac' for elem in my_list}
print('my_dict: ' + str(my_dict))

# Condition in generator
my_list_2 = [elem for elem in my_list if elem % 2 != 0 and elem > 0]
print('my_list_2: ' + str(my_list_2))

# Double 'for' loop in generator
# 'join()' unites address with filename
path = input('Enter your path: ')
files_by_path = [os.path.join(addresses, file)
                 for addresses, dirs, files in os.walk(path)
                 for file in files if '.txt' in file]
print('Count of files with .txt extension in ' +
      str(path) + ' is ' + str(len(files_by_path)))

# Dictionary generator on the basis of another dictionary
prices = {'bread': 0.59, 'milk': 0.99, 'water': 0.79, 'meat': 4.89}
print('Old prices: ' + str(prices))

# Making 5% discount on all products
new_prices = {price: round(prices[price] * 0.95, 2) for price in prices.keys()}
print('New prices: ' + str(new_prices))

''' Generator expression '''

# Declaring different URLs
url_list = ['https://www.youtube.com', 'https://www.google.com',
            'https://pkgs.org', 'https://github.com', 'https://www.codewars.com']
# List generator
sites_name = [site_name.split('//')[1]
              for site_name in url_list if '.com' in site_name]
print(type(sites_name))
print(sites_name)
# Generator expression
# Allows to process one by one
sites_name = (site_name.split('//')[1]
              for site_name in url_list if '.com' in site_name)
print(type(sites_name))

# Iteration generator with 'for' loop
for site_name in sites_name:
    print(site_name)

''' Generator function '''

# Typical function
def read_lines(file):
    ''' Reading file line by line. Returns file content as list of words '''
    list_text = []
    with open(file, 'r', encoding='UTF-8') as f:
        for sentence in f:
            word = sentence.split('\n')
            list_text.append(word)
    return list_text

# Generator function
def read_lines_gen(file):
    ''' Reading file line by line. Returns file content as list of words '''
    list_text = []
    with open(file, 'r', encoding='UTF-8') as f:
        for word in f:
            yield word

call_gen = read_lines_gen('text.txt')

# Printing text while not '\n', so printing paragraphs
for i in call_gen:
    print(i)

# Opening file
with open('text.txt', 'w') as file:
    # Writing data into a file
    file.write('Kali Linux is an open-source, Debian-based Linux distribution geared' +
               'towards various information security tasks, such as Penetration Testing, Security ' +
               'Research, Computer Forensics and Reverse Engineering.' + 
               '\nThe BeagleBone Black provides a microSD card slot for mass storage and ' +
               'if that device is bootable, will use it in preference to the board\'s “burned-in” Angstrom or Debian operating system.')

print(read_lines('text.txt'))

# Deleting text.txt
print('Do you want to delete files which was used in this program? ')
while True:
    is_delete = input('y/n: ')
    if is_delete == 'Y' or is_delete == 'y':
        os.remove('text.txt')
        print('File text.txt has been removed')
        break
    elif is_delete == 'N' or is_delete == 'n':
        print('File text.txt hasn\'t been removed')
        break
    else:
        print('Incorrect data input. Try again: ')
