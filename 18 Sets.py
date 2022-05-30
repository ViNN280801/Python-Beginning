### Important remark: if you don't have colorama, just execute this command
### pip install colorama

# Importing 'time' module
import time

# Importing 'os' module
import os

# Importing 'colorama' module
import colorama
# Importing submodule 'Fore' from 'colorama'
from colorama import Fore

# Set can initialized by curve brackets {} or 'set()' function
# Set can consist of constant data types: number, tuple, string
set_1 = {'kqd', 91, 75, 9, '19sq',  (5, 4.15), (1.93, 'gtd')}
print('set_1: ' + str(set_1))

# If you try to add same values, set will remove it, because set contains only unique elements, non-recurring
# Function 'set()' automatically sort set
set_2 = set([(0, 1, 5), 9, 4, 7, 7, 7, 7, 1, 9, (1, 6, 9)])
print('set_2: ' + str(set_2))

# Returns list contains from objects which didn't exist before


def foo(*args):
    list = []
    for i in args:
        for j in i:
            if j not in list:
                list.append(j)
    return list


# Initializing 3 list
list_1 = list(range(10000))
list_2 = list(range(5000, 15000))
list_3 = list(range(10000, 20000))

''' print('\nExperiment 1: ')
# Using method 'time()' to track how much time has passed
# Declaring start time of executing operation
time_before = time.time()
# Calling 'foo()' function
foo(list_1, list_2, list_3)
# Calculation defference between stop time and start time to get time of working 'foo()' function
result_time = time.time() - time_before
print(str(result_time) + 's needed for executing function of appending objects which didn\'t exist before in list')
 '''

print('\nExperiment 2: ')
# Declaring start time of executing operation
time_before = time.time()
# Redefining 'set_1' with values from 'list_1'
set_1 = set(list_1)
# Combine sets which contains values from 'list_1', 'list_2' and 'list_3' using 'union()' method
set_2 = set_1.union(set(list_2), set(list_3))
# Calculation defference between stop time and start time to get time of combining lists into set
result_time = time.time() - time_before
print(str(result_time) +
      's needed for combine values from all lists into one single set')

# Clearing both of sets
set_1.clear()
set_2.clear()

# Reinitializing previous set
set_1 = {'kqd', 91, 75, 9, '19sq',  (5, 4.15), (1.93, 'gtd')}
print('\nset_1 before adding: ' + str(set_1))
# Adding element to set using 'add()' method
set_1.add(89)
print('set_1 after adding: ' + str(set_1))
# Deleting element from set using 'discard()' method
set_1.discard((5, 4.15))
print('set_1 after deleting with \'discard()\' methtod:\n' + str(set_1))
# Deleting element from set using 'remove()' method
set_1.remove('19sq')
print('set_1 after deleting with \'remove()\' method:\n' + str(set_1))
# Reinitialize 'set_2'
set_2 = set([(0, 1, 5), 9, 4, 7, 7, 7, 7, 1, 9, (1, 6, 9)])
print('set_2: ' + str(set_2))
# Combining two sets using 'union()' method
set_1 = set_1.union(set_2)
print('set_1 after combining with set_2 using \'union()\' method:\n' + str(set_1))

# Reinitializing previous set
set_1 = {'kqd', 91, 75, 9, '19sq',  (5, 4.15), (1.93, 'gtd')}
print('\nset_1: ' + str(set_1))
# Reinitialize 'set_2'
set_2 = set([(0, 1, 5), 9, 4, 7, 7, 7, 7, 1, 9, (1, 6, 9)])
print('set_2: ' + str(set_2))
# Combining two sets using 'update()' method
set_1.update(set_2)
print('set_1 after combining with set_2 using \'update()\' method:\n' + str(set_1))
# Reinitializing previous set
set_1 = {'kqd', 91, 75, 9, '19sq',  (5, 4.15), (1.93, 'gtd')}

# Find common elements of sets using 'intersection()' method
common_elements = set_1.intersection(set_2)
print('\nCommon elements in both of sets:\n' + str(common_elements))

# Find difference between set
# 'difference()' method shows which values in set A do not occur in set B
# Where A is 'set_1', B is 'set_2'
different_elements = set_1.difference(set_2)
print('\nThese elements from the set_1 don\'t occur in set_2:\n' +
      str(different_elements))
different_elements = set_2.difference(set_1)
print('These elements from the set_2 don\'t occur in set_1:\n' +
      str(different_elements))

# Let's create text file to do syntax analyze of it
# Open (create if it isn't exist) file in write mode
text_file = open('text_file.txt', 'w')
# Writing text into file
text_file.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse posuere augue eros. Duis nisl nulla, suscipit' +
                'id condimentum sit amet, facilisis vel elit. Aenean scelerisque ex dolor, at fringilla lacus rhoncus nec. Phasellus dolor ' +
                'lectus, maximus quis scelerisque at, euismod et arcu. Mauris et mauris hendrerit, pharetra velit id, malesuada risus. ' +
                'In blandit mi risus. Curabitur dui nibh, ullamcorper in tristique eget, semper nec ex. Mauris id nulla eget justo auctor ' +
                'congue vel eu lectus. Integer sodales semper felis, a egestas elit tristique a. Phasellus at ultricies elit, non porttitor purus. ' +
                'Nam tristique neque a quam lacinia dapibus. Nullam eget urna in justo malesuada imperdiet.\nSed quis nibh eget nisl ' +
                'luctus porttitor. Maecenas vestibulum iaculis sem eu tincidunt. In hac habitasse platea dictumst. Mauris malesuada mauris ' + 
                'et enim efficitur pellentesque. Nullam eget pretium arcu. Vestibulum in bibendum elit, id dapibus risus. Pellentesque ' + 
                'ac malesuada sem. Nulla facilisis odio at lacus consequat varius. Sed pulvinar aliquam feugiat. Aliquam sit amet accumsan odio. ' + 
                'Duis lobortis urna leo. Pellentesque auctor arcu at aliquet congue. Cras viverra non justo interdum pharetra.\nIn ' +
                'pellentesque, dui eget maximus porta, est elit venenatis lectus, vel dapibus diam felis ac dui. Nullam velit purus, condimentum ' +
                'id consectetur eu, luctus ac ex. Maecenas sed ante eu neque tincidunt viverra nec ac ipsum. Duis gravida risus elit, ' +
                'non feugiat tellus bibendum non. Cras posuere, urna eget tempus finibus, ante sapien mollis leo, quis vestibulum felis ' +
                'quam nec tortor. Morbi elementum eros sed tempus sollicitudin. Sed euismod vehicula egestas. Aliquam tincidunt tincidunt ' + 
                'lacus, id placerat nisl laoreet sit amet. Aenean a malesuada neque.\n Morbi porta fringilla mi, ut cursus est pharetra luctus. ' +
                'Aenean rhoncus porttitor scelerisque. Ut justo quam, scelerisque vitae posuere a, tempor ac eros. Quisque vel dolor ' +
                'maximus, facilisis nisl in, pellentesque sapien. Donec ornare congue elit accumsan venenatis. Pellentesque id sem hendrerit, ' +
                'tempor erat eget, condimentum velit. Proin libero sapien, dictum a leo ut, blandit ornare justo. Etiam mi enim, imperdiet vel ' + 
                'tempor sit amet, lobortis eget ex. Praesent volutpat, ante at placerat mattis, mauris odio porta ligula, eget malesuada elit ' + 
                'dolor non justo. Donec cursus tellus hendrerit sapien faucibus sodales. Sed mattis at nibh et volutpat. Etiam ultricies dolor ' + 
                'a velit convallis, nec consectetur quam lobortis.\nAliquam erat volutpat. Donec id purus mauris. Quisque a lorem eu urna tristique ' + 
                'pharetra vel luctus dolor. Integer lobortis gravida neque, in imperdiet tellus efficitur sed. Vivamus aliquet, leo in molestie ' + 
                'laoreet, sapien risus venenatis augue, posuere tincidunt sapien est id arcu. Praesent efficitur pellentesque dui et scelerisque. ' + 
                'Aenean pharetra orci non mattis pharetra. Mauris faucibus ornare ornare. Suspendisse egestas arcu non mauris consequat, ' + 
                'sit amet blandit nibh commodo. Nam a molestie elit, sed fermentum est. Fusce porta, purus at ultricies accumsan, quam purus ' +
                'hendrerit sapien, tempus bibendum eros quam ut libero. In fermentum diam sit amet sem porttitor, vitae auctor nulla efficitur. ' +
                'Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Aenean at magna vel leo mollis ' +
                'semper. Aenean vitae mauris ut nulla varius efficitur. Donec interdum pellentesque diam ut maximus.\n')
# Closing file
text_file.close()

### Following code designed for black terminal background

# We need to create list without repeated words
text_file = open('text_file.txt', 'r')
print('\nText ' + Fore.RED + 'before' + Fore.WHITE + ' converting to set:\n' + str(text_file.read()))
# Closing file
text_file.close()
# Open file to read data from it
text_file = open('text_file.txt', 'r')
# 1st step: splitting text on words
# 2nd step: reading text from file
# 3rd step: convert recieved list of splitted words to set (as we remember, 'set()' function will discard repeated words)
unique_words = set(text_file.read().split())
print('\nText ' + Fore.RED + 'after' + Fore.WHITE + ' converting to set:\n' + str(unique_words))
# Closing file
text_file.close()

# Opening text_file.txt in write mode. All content will be removed
text_file = open('text_file.txt', 'w')
# Rewriting text_file.txt with parsed (unique) words using 'for' loop
print('\nRewriting text_file.txt ...')
for word in unique_words:
    text_file.write(str(word) + ' ')
print('text_file.txt rewritten')
# Closing file
text_file.close()

# Deleting file text_file.txt if it's no longer needed
print('\nDo you want to delete text_file.txt which uses in work of this program? ')
# For do that we have infinite loop
while True:
    # Initializing variable which will store choice of user
    is_delete = input('y/n: ')
    # If user entered 'Y' or 'y' -> delete file text_file.txt using 'remove()' method from 'os' module
    if is_delete == 'Y' or is_delete == 'y':
        os.remove('text_file.txt')
        print('File text_file.txt has been removed')
        # Breaking loop
        break
    # If user entered 'N' or 'n' -> just break the loop
    elif is_delete == 'N' or is_delete == 'n':
        print('Exiting')
        break
    # Protection from incorrect data
    else:
        print('Entered string is invalid. Try again')    
