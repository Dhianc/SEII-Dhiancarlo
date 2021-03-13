if True:
    print('Conditional was True')

language = 'Python'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

language = 'Java'
if language == 'Python':
    print('Language is Python')
else:
    print('No match')

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No match')

user = 'Admin'
logged_in = False
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'Admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if not logged_in:
    print('Please log in')
else:
    print("Welcome")

a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)
print(a is b) #id(a) != id(b) não são a mesma lista

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = None
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = 0 #Qualquer outro valor é True
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')

condition = ''
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')