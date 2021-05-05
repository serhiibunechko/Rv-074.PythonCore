import math
from math import*


choice = int(input(
    'Press 1 if you want to calculate area of rectangle\n'
    'Press 2 if you want to calculate area of triangle\n'
    'Press 3 if you want to calculate area of circle\n'))
if choice == 1:
    a = float(input('Plz enter length of first side:    '))
    b = float(input('Plz enter length of second side:    '))
    S = a*b
    print('S = ', S)
elif choice == 2:
    a = float(input('Plz enter length of 1 side: '))
    b = float(input('Plz enter length of 2 side: '))
    c = float(input('Plz enter length of 3 side: '))
    p = (a + b + c)/2
    S = sqrt(p*(p-a)*(p-b)*(p-c))
    print('S = ', S)
elif choice == 3:
    radius = float(input('Plz enter radius: '))
    S = radius * (math.pi ** 2)
    print('S = ', S)
