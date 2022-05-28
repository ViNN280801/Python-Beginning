m = [1, 2, 1, 3, 4]
print(type(m))

for i in m:
    print(i)
print('\nSize of list = ' + str(len(m)) + ' elements')

print('m[-1] = ' + str(m[-1]))

m_2 = [1, 2, 2, 4, 'Some string', [
    'string_* 1', 'str # !2'], [4.5, 9.623, 7.56]]

count = 0
print()
for i in m_2:
    print('m_2[' + str(count) + '] = ' + str(i))
    count += 1

m_2[4] += ' concatenated'

# Swap:
m_2[1], m_2[6] = m_2[6], m_2[1]

print('\nList after transform: ')
for i in m_2:
    print('m_2[' + str(count) + '] = ' + str(i))
    count += 1

print('\nNemyListt list: ')
n = list('Some string ' + str(5.34) + 'f' + str(8))
myList = []

for i in n:
    if i == str(8):
        continue
    else:
        myList += [i]
else:
    print(n)
    print(myList)