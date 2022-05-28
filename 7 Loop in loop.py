alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWmyListYZabcdefghijklmnopqrstuvwmyListyz'

userString = input('Enter string: ')
count = int(0)

for charInAllChars in alphabet:
    for charInUsersString in userString:
        if charInAllChars == charInUsersString:
            count += 1

if int(count) == 1:
    print('There is ' + str(count) + ' symbol from latin alphabet')
else:
    print('There is ' + str(count) + ' symbols from latin alphabet')

print('1st range(): ')
# range() generating 10 values (from 0 to 9)
for myList in range(10):
    print(myList)

print('2nd range(): ')
# range() generating values from 5 to 9
for myList in range(5, 10):
    print(myList)

print('3rd range(): ')
# range() generating values from 10 to -8 with step = -2
for myList in range(10, -10, -2):
    print(myList)