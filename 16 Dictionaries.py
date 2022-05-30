# Initializing empty dictionary using curve brackets
dict_1 = {}
# Initializing empty dictionary using "dict()"
dict_2 = dict()
# Initializing dictionary using "dict.fromkeys('_value_')"
dict_3 = dict.fromkeys('dictionary_value')

# Initializing dictionary with curve brackets
# On the left side dictionary has a key, on the right side is value which is assigned to this key
products_price = {'bread': 1.99, 'milk': 2.05, 'meat': 5.59, 'water': 0.99}

# Initializing dictionary of users
users = {'James': {'id': 1, 'psswd': '@43hfiuoH#*2o3i'},
         'Ann': {'id': 2, 'psswd': 'snlji43iofp3@0183'},
         'Robert': {'id': 3, 'psswd': '032439if__12uhu3!!Shd'},}

# Returns result sum of products
def product_buy():
    print(products_price)
    print('What do you want to buy? ')
    print('If you want to end buying products enter \'end\'')
    sum = 0
    while True:
        products_list = input()
        if(products_list == 'end'):
            break
        sum += products_price[products_list]
    return sum

print('Amount of purchase is ' + str(float(product_buy())) + '$')

# Copying data from 'users' to 'dict_1'
print('\'dict_1\' = ' + str(dict_1))
print('\'users\' = ' + str(users))
print('Copying data from \'users\' to \'dict_1\':')
dict_1 = users.copy()
print('\'dict_1\' = ' + str(dict_1))

# Get items of dictionary using 'items()' method
print('\nGetting items from \'products_price\': ' + str(products_price.items()))

# Get keys of dictionary using 'keys()' method
print('\nGetting keys from \'products_price\': ' + str(products_price.keys()))

# Get values of dictionary using 'values()' method
print('\nGetting values from \'products_price\': ' + str(products_price.values()))

print('\nUpdating \'dict_1\' with values in \'dict_2\'')
# Clearing dictionaries
dict_1.clear()
dict_2.clear()
# Filling dictionaries with items
dict_1 = {'a' : 1, 'b' : 2, 'c' : 3}
dict_2 = dict([[1, 2], [3, 4], ['c', 1]])
# Printing dictionaries
print('\'dict_1\' = ' + str(dict_1) + '\n' + '\'dict_2\' = ' + str(dict_2))
dict_1.update(dict_2)
# How we see in output, if one dictionary contains same item, it's item will be modified be 'update()' method
# if other dictionary don't has same items they will be added
print('Updated \'dict_1\' = ' + str(dict_1))

# Checking for availibiity in dictionary
if 'b' in dict_1:
    # Getting access in dictionary by it's key and square brackets
    print('\nChecking \'b\' value in dictionary: ' + str(dict_1['b']))

# Getting value from dictionary using 'get()' method
print('\nGetting value from dictionary: \'a\' : ' + str(dict_1.get('a')))
# If there is no such value, 'get()' will return 'None'
print('Getting value from dictionary: \'k\' : ' + str(dict_1.get('k')))
# If you want to change 'None' you need to pass your own value with the 2nd parameter
print('Getting value from dictionary: \'k\' : ' + str(dict_1.get('k', 'My own value')))

# Removing item from dictionary using 'pop()' method
# Note: 'pop()' method can returns value
print('\n\'dict_1\' = ' + str(dict_1))
# Removing item
dict_1.pop('b')
print('Removing \'b\' item from \'dict_1\':')
print('\'dict_1\' = ' + str(dict_1))
# Keep removed item to value
removed_item = dict_1.pop('a')
print('Removed item is ' + str(removed_item))
print('\'dict_1\' = ' + str(dict_1))

# Dictionary iteration with 'for' loop
# Iteration will occur by keys
print('\nIteration in dictionary: ')
for i in products_price:
    print(i)

print('\nPrices without discount:\n' + str(products_price))
# Make discount 10% on all goods:
print('Iteration in dictionary: ')
for i in products_price:
    products_price[i] *= 0.9
    # Rounding up to the 2nd sign: 1.791 -> 1.79
    products_price[i] = round(products_price[i], 2)
print('Prices with 10% discount:\n' + str(products_price))

# Splitting dictionary on tuples of items using 'for' loop
print('\nSpliiting dictionary on tuples of items: ')
for item in products_price.items():
    print(item)

# Splitting dictionary on keys and values using 'for' loop
print('\nSpliiting dictionary on keys and values: ')
for key, value in products_price.items():
    print('key = ', key,  '; value = ', value, '$')

# Reversing dictionary using 'for' loop
reversed_dict = {}
for key, value in products_price.items():
    reversed_dict[value] = key
print('\nOroginal dictionary:\n' + str(products_price))
print('Reversed dictionary:\n' + str(reversed_dict))
