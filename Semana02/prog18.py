'''
LEGB
Local, Enclosing, Global, Built-in
'''

x = 'global x'

def test():
    y = 'local y'
    print(y)
    print(x)

test()
print(x)
#print(y) //é variável local e não é impressa aqui

print('')
x = 'global x'

def test():
    global x
    x = 'local x'
    print(x)

test()
print(x)

print('')
def test(z):
    x = 'local x'
    print(z)
    
test('local z')

print('')
import builtins

#print(dir(builtins)) //to show commands

def my_min():
    pass

m = min([5, 1, 4, 2, 3])
print(m)

print('')
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)

    inner()
    print(x)
outer()

print('')
def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)
        
    inner()
    print(x)
outer()

x = 'global x'
print('')
def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
        
    inner()
    print(x)
outer()
print(x)