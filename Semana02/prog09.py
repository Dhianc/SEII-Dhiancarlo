import my_module

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index)

import my_module as mm

courses = ['History', 'Math', 'Physics', 'CompSci']

index = my_module.find_index(courses, 'Math')
print(index)

from my_module import find_index, test

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
print(index)
print(test)

print('')
import sys
print (sys.path)

print('')
import random
random_course = random.choice(courses)
print(random_course)

print('')
import math
rads = math.radians(90)
print(rads)
print(math.sin(rads))

print('')
import datetime
import calendar
today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

print('')
import os
print(os.getcwd())
print(os.__file__)

import antigravity #abre página web 