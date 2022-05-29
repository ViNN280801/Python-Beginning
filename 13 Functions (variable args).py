# Prints recieved parameters
def name(param1, param2, *args, key):
    print(param1)
    print(param2)
    print(args)
    print(key + ' = ' + str(25))

name(4, 6, 2, 6, 6, 1, 9, 2, 3, key = 'key')

# Returns complecated list, if 'is_sort' is True - sorts 'new_list'
def exclusive_item(*args, is_sort = False):
    new_list = []
    for i in args:
        for j in i:
            if j not in new_list:
                new_list.append(j)
    if is_sort == True:
        new_list.sort()
    return new_list

# Initializing three lists
list_1 = [9, 1, 5]
list_2 = [5, 5, 1, 8, 0, 6, 5]
list_3 = [1, 2, 3, 5, 9, 2, 0, 5, 3, 7, 8, 9]

# Checking work of functions
temp = exclusive_item(list_1, list_2, list_3, is_sort = False)
print(temp)
temp.clear()
temp = exclusive_item(list_1, list_2, list_3, is_sort = True)
print(temp)
