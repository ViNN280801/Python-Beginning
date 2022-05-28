print('Tuple: ')
print('Tuple is constant, faster iterating by cycles, taking up less space in memory')
# Initializing tuple type
myTuple = (9, 3, 6, 1, 8, 0)
# Printing type
print(type(myTuple))
# Printing tuple
print(str(myTuple) + '\n')

# Another way to initialize tuple:
print('Another tuple initialized by tuple() method: ')
# Initializing and converting another tuple
myTupleAnother = tuple(['abc', 5, 1, 5.0])
print(str(myTupleAnother) + '\n')

# Declaring list to copy tuple into
myTupleCopy = []

print('Copying data from tuple to list using \'for\' loop and append() method, then modify each value (+3): ')
# Copying tuple to list with modifying elements using 'for' loop
for i in range(len(myTuple)):
    myTupleCopy.append(myTuple[i] + 3)

# Printing relevant tuples
print('Tuple before copying: ' + str(myTuple))
print('Tuple after copying: ' + str(myTupleCopy) + '\n')

print('Modifying data in tuple: ')
# Copying data to 'myTupleAnother' from 'myTuple' to show differnece between original tuple and modified tuple
myTupleAnother = tuple(myTuple)
# Initializing 'modify' list
modify = list(myTuple)
# Modifying 3rd element
modify[2] = 45
# Converting back to tuple
myTuple = tuple(modify)
print('Original tuple: ' + str(myTupleAnother))
print('Modified tuple: ' + str(myTuple) + '\n')

print('Adding new tuple to existing tuple using operator +=: ')
# Initializing tuple to concatenate
myTupleToAdd = ('0b.1117', 'IEN.901', 9.0, 4, 7)
# Printing original tuple and tuple which we want to add to existing original tuple
print('Original tuple: ' + str(myTuple))
print('Tuple to append: ' + str(myTupleToAdd))
# Concatenating tuples with "+="
myTuple += myTupleToAdd
# Printing result, concatenated, tuple
print('Result tuple: ' + str(myTuple) + '\n')

# Conclusion: we can adding tuple to tuple but modifying is restricted
