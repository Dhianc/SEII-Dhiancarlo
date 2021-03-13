student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print('\n',student['name'])

print(student.get('phone', 'Not Found'))

student['phone'] = '555-5555'
student['name'] = 'Jane'
print('\n',student)

student.update({'age': 23, 'phone': '555-0000'})
print('\n',student)

del student['age']
print('\n',student)

phone = student.pop('phone')
print('\n',phone)
print(student)

print('\n',len(student))

print('\n',student.keys())
print(student.values())

print('\n',student.items())

print('\n')
for key in student:
    print(key)

print('\n')
for key, value in student.items():
    print(key, value)