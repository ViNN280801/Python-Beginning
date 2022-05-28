a = None
print('a = ', a, 'Type =', type(a))
a = 1
print('a = ', a, 'Type =', type(a))
a = 1.0
print('a = ', a, 'Type =', type(a))
a = 1 + 1j
print('a = ', a, 'Type =', type(a))
a = '1'
print('a = ', a, 'Type =', type(a))
a = "1"
print('a = ', a, 'Type =', type(a))
a = [1, 1, 1]
print('a = ', a, 'Type =', type(a))
a = [1, 1, 'a']
print('a = ', a, 'Type =', type(a))
a = {1, 2, 3}
print('a = ', a, 'Type =', type(a))
a = {1, 2, 'a'}
print('a = ', a, 'Type =', type(a))
a = {'a' : 1, 'b' : 2}
print('a = ', a, 'Type =', type(a))
a = True
print('a = ', a, 'Type =', type(a))

str = 'string'
to = 'to'
concatenate = 'concatenate'
result = str + ' ' + to + " " + concatenate
print(result)

x = input('Enter the number: ')
print('Recieved data has ', type(x), ' type.')
r = int(x) + 5
print(r)
float_var = float(5)
print(float_var)

num_1 = input('Enter 1st number: ')
num_2 = input('Enter 2nd number: ')
sum = int(num_1) + int(num_2)
print('Result of sum is ', sum)
