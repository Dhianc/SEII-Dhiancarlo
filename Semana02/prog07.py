nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 3:
        print('found!')
        break
    print(num)

print('')
for num in nums:
    if num == 3:
        print('found!')
        continue
    print(num)

print('')
for num in nums:
    for letter in 'abc':
        print(num, letter)

print ('')
for i in range(10): 
    print(i)

print ('')
for i in range(1, 11): #começa em 1 e nao inclui o 11
    print(i)

print ('')
x = 0
while x < 10:
    print(x)
    x += 1

print ('')
x = 0
while True:
    if x == 5:
        break
    print(x)
    x += 1