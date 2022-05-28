x = input('Enter number: ')

if int(x) == 0:
    print('Value equals null')
elif int(x) > 0:
    print('Value is positive')
else:
    print('Value is negative')

print(x)

a = 'a'

if a == 0:
    a = 1
    print('a was equals 0')
elif type(a) == type(1) or type(a) == type(1.1):
    print('a is valid data type')
else:
    print('a is invalid data type')
    a = 1

print((100 / float(a)) / 4.3)