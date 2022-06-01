# Common function (just for example)
def greetings():
    # Printing greetings
    print('Good to see you')

# Another common function
def division(divisible, divider):
    # Returns quotient
    try:
        return float(divisible) / float(divider)
    except:
        print('Divider and divisible are not a numbers or divider equals null')


divisible = input('Enter divisible: ')
divider = input('Enter divider: ')
print('Using common function:')
print('Result of division is ' + str(division(divisible, divider)))

# Lambda function
quotinent = lambda divisible, divider: divisible/divider
print('\nUsing lambda function:')
print('Result of division is ' + str(quotinent))

### Sorting using common function

# Initiazlizing complecated list
complicated_list = [['Prvt', 'Joseph Allen', 1994], ['Cpt', 'Johnatan Price', 1985], ['Lt', 'Symon Riley', 1990]]

# Common function for sort
def sort_complicated_list(param):
    return param[1]

sorted_list = sorted(complicated_list, key=sort_complicated_list)
print(sorted_list)

### Sorting with lambda function

# Initiazlizing complecated list
complicated_list = [['Prvt', 'Joseph Allen', 1994], ['Cpt', 'Johnatan Price', 1985], ['Lt', 'Symon Riley', 1990]]
sorted_list = sorted(complicated_list, key=lambda x : x[1])
print(sorted_list)

# Using with function 'filter()'
x = list(filter(lambda x : x[2 ] > 1990, complicated_list))
print(x)
