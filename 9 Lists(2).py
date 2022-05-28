myList = [9, 8, 4, 6, 1]
print('List: ')
print(str(myList) + '\n')

print('Adding 2 to the end of list using append() method: ')
myList.append(2)
print(str(myList) + '\n')

print('Adding 3 in 0 position (indemyList) of list using insert() method: ')
myList.insert(0, 2)
print(str(myList) + '\n')

print('Showing how many idential elements (2) in list using count() method: ')
myList.append(2)
print('In list ' + str(myList.count(2)) + ' idential elements which equals 2')
print(str(myList) + '\n')

print('Sorting list in ascending order using sort() method: ')
myList.sort()
print(str(myList) + '\n')

print('Reversing list using reverse() method: ')
myList.reverse()
print(str(myList) + '\n')

print('Removing last element using pop() method without arguments: ')
myList.pop()
print(str(myList) + '\n')

print('Removing last element using pop() method with index 2: ')
myList.pop(2)
print(str(myList) + '\n')

print('Adding to existed list new list using operator +=: ')
myList += [5, 8, 6, 0, 1, 3, 5, 6]
print(str(myList) + '\n')

print('Removing element by it\'s value using remove() method: ')
myList.remove(9)
print(str(myList) + '\n')

print('Clearing all list using clear() method: ')
myList.clear()
print(str(myList) + '\n')

print('Adding values from another list using extend() method: ')
myList.extend([5, 3, ['abc', 'zero'], [4.0, 1.21, 9.59]])
print(str(myList) + '\n')

print('List which will be used for splitting on two other lists with odd and even integer values: ')
templateList = list(range(1, 21, 1))
print(str(templateList) + '\n')

# Initializing another lists
odd = []
even = []

# Splitting 'templateList' on two other lists in 'for' loop
for i in templateList:
    if i % 2 != 0:
        odd.append(i)
    else:
        even.append(i)

print('List with odd values: ')
print(str(odd) + '\n')
print('List with even values: ')
print(str(even) + '\n')

# Zeroing out all declared lists
odd.clear()
even.clear()
myList.clear()

print('Copying all elements from one list to another list using copy() method: ')
myList = [str(5), 1, int(93.7), ['elem_3', 'nice', 67], 0, 4,
          float(1), 5, [4.1534, 5.78, float(1), float(0)]]
print('Count of elements in list = ' + str(len(myList)) + '\n')
myListCopy = myList.copy()
print(str(myListCopy) + '\n')

# Clear myListCopy
myListCopy.clear()
print('Copying all elements using "src = dest[::]": ')
myListCopy = myList[::]
print(str(myListCopy) + '\n')

# Clear myListCopy
myListCopy.clear()
print(
    'Copying certain elements (from _begin_ to _end_ with _step_ step) using src = dest[_begin_:_end_:_step_]: ')
myListCopy = myList[5:9:1]
print(str(myListCopy) + '\n')

myList.clear()
myListCopy.clear()

print('Separating list using "src = dest[_begin_::_step_]"')
myList = list(range(1, 26))
print('List before separating: ' + str(myList) + '\n')

# Getting odd elements in list
myList = myList[0::2]
print('List arter separating: ' + str(myList) + '\n')
