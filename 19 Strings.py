# Importing 'string' module
import string

# Initializing string with quotes
my_str = 'Let\'s write as \'str\''
# Printing string
print(my_str)

# If you don't want escaping string, write 'r' literal before initialization of string
my_str = 'Some new\nstring'
print(my_str)
my_str = r'Some new\nstring'
print(my_str)

# Printing from 2nd character to 6th character
print(my_str[2:6])

# Printing if substring exists in string
print('ew' in my_str)

# Make all characters to upper case using 'upper()' method
print(my_str.upper())


# Make all characters to lower case using 'lower()' method except first string
my_str[0:].lower()
print(my_str)

# Another way to make all characters to lower case using 'lower()' method except first string
print(my_str.upper())
print(my_str.capitalize())

my_str = ('DICT, FILE, FTP, FTPS, GOPHER, GOPHERS, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, ' +
       'RTMP, RTMPS, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET and TFTP. curl supports SSL certificates, HTTP ' +
       'POST, HTTP PUT, FTP uploading, HTTP form based upload, proxies, HTTP/2, HTTP/3, cookies, user+password authentication ' +
       '(Basic, Plain, Digest, CRAM-MD5, SCRAM-SHA, NTLM, Negotiate and Kerberos), file transfer resume, proxy tunneling and more.')

print('\nString before replace comma: ' + my_str + '\n')
# Replacing all comma (,) to semicolon (;)
print('String after replace comma: ' + my_str.replace(',', ';'))

# Reversing string
my_str = 'Hello, World!'
print('\nString before reverse: ' + my_str)
my_str = my_str[::-1]
print('String after reverse: ' + my_str)

# Remove all punctuation using module 'string' and 'string.punctuation'
my_str = 'Thi}s str.in(g c-on_tain()s to__o ma?ny p!un>ctuation. we nee...d to remo!v??e i!?><t'
print('\nString before deleting punctuation: ' + my_str)
for punct in string.punctuation:
    if punct in my_str:
        my_str = my_str.replace(punct, '')
print('String after deleting punctuation: ' + my_str)

# Splitting string in list by spaces
str_list = my_str.split(' ')
print('\nString after splitting converts to list:')
print(str_list)

# Assembly string from list using 'join()' method
# ' ' - is separator string which will be used in string 'my_str', 'join()' will complicate string from list
my_str = ' '.join(str_list)
print('\nString after assembly: ' + my_str) 

# f-strings
name = input('Enter your name: ')
# Concatenate string using operator '%s'
my_str = 'Hello, %s!' % name
print(my_str) 
# If we want to add in string several strings, we need to write their like a tuple
name = input('Enter your name: ')
my_str = 'Hello, %s! My name is %s' % (name, 'Python')
print(my_str) 
# Another way using 'format()' method
name = input('Enter your name: ')
my_str = 'Hello, {}! My name is {}'.format(name, 'Python')
print(my_str) 
# Interesting thing with indeces
# {1} means that the 1st value from tuple will be substituted in this place
name = input('Enter your name: ')
my_str = 'Hello, {1}! My name is {0}'.format(name, 'Python')
print(my_str)
# Newest way to format strings using f-strings (f'my_string')
name = input('Enter your name: ')
my_str = f'Hello, {name}!'
print(my_str)
