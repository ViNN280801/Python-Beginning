counter = 0

while counter < 5:
    print('counter = ', counter)
    counter += 1
else:
    print('From eles: While has ended')

while True:
    number = int(input('Enter number: '))

    counter = 0
    fact = 1

    while counter < number:
        counter += 1
        fact *= counter
    else:
        print('Factorial of ' + str(number) + ' = ' + str(fact))
