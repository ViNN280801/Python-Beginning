# Importing 'os' and 'time' modules
import os
import time

# Initializing empty list
list = []

# Splitting all recieved tuples from walk() method to 3 variables
for address, dirs, files in os.walk(input('Enter your path: ')):
    for file in files:
        # 'path' - common pathname manipulations
        # method join() - joins one or more paths components intelligently. The return value is 
        # the concatenation of path and any members of *paths with exactly one directory separator 
        # following each non-empty part except the last, meaning that the result will only end in a 
        # separator if the last part is empty. If a component is an absolute path, all previous 
        # components are thrown away and joining continues from the absolute path component.
        name = os.path.join(address, file)
        
        # Method time() returns time from beginning of epoch
        # Return the system’s ctime which, on some systems (like Unix) 
        # is the time of the last metadata change, and, on others (like Windows), is the creation time for path
        # Compare result time with 86400 seconds (1440 minutes -> 24 hours)
        if '.py' in name and time.time() - os.path.getctime(name) < 86400:
            list.append(os.path.join(address, file))

if list == []:
    print('There is no files with name ends with .txt')
else:
    print(list)