# Declaring functions
def show():
    print('Text')


def show2():
    x = 7
    return x


# Calling function show()
show()

# Calling second function
y = show2()
print(y)

# Defining my length function
# 'count' is default parameter
def length(param1, param2=False, count=0):
    if param2 == True:
        param1Type = type(param1[0])
        for i in param1:
            count += 1
        # Returns tuple
        return count, param1Type
    else:
        for i in param1:
            count += 1
        return count


list = [9, 6, 5, 1, 4]
print(length(list))
list.clear()
list = [9]
print(length(list))
list.clear()
list = ['1', 'f', '=']
print(length(list, True))