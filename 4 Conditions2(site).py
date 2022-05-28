import os
import time
import webbrowser

site = input('Enter name of site you want to open: ')
url = 'www.' + site

if 'https://' in url or 'www.' in url:
    print('Opening ' + site)
    webbrowser.open(url)
else:
    print('There is no such site.')

print('Starting gimp ... ')
time.sleep(1)
os.system('gimp')
