count = 0

for i in 'String of temyListt':
    print('i = ' + i)

    if(i == 't'):
        print('\'t\' found in string')
        count += 1
else:
    print('String have ' + str(count) + ' \'t\' characters')
    print('Loop \'for\' has ended')
