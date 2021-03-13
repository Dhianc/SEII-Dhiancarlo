print('Hello World\n')

message = 'Hello World\n'
print(message)

message = """Bobby's World was a good
cartoon in 1990's\n"""
print(message)

message = 'Hello World\n'
print(len(message))

print(message[0])

print(message[:5])

print(message[6:])

print(message.lower())

print(message.upper())

print(message.count('l'))

print(message.find('World'))

print(message.find('Universe'))

new_message = message.replace('World', 'Universe')
print(new_message)

greeting = "Hello"
name = 'Michael'
print(greeting + ', ' + name + '. Welcome!')

message = '{}, {}. Welcome!'.format(greeting, name)
print(message)

message = f'{greeting}, {name.upper()}. Welcome!'
print(message)
