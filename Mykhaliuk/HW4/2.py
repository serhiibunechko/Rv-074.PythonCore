#Depending on the user's choice, calculate the square of ​​either a rectangle, or a triangle,
#or a circle. If a rectangle or triangle is selected,
#the lengths of the sides should be invited; is circle, its radius.
from math import pi
figure = input('Chose a figure to work with:\n(1)Square (2)Rectangle (3)Triangle (4)Circle:')

if figure=='1': 
    sides = int(input("Enter 1 side length: "))
    perimetr = sides*4 
elif figure=='2':
    sides = (input("Enter 2 side lengths with space in between: ").split())
    perimetr = ((int(sides[0]) + int(sides[1])) *2)
elif figure=='3':
    sides = (input("Enter 3 side lengths with spaces in between: ").split())
    perimetr = (int(sides[0]) + int(sides[1]) + int(sides[2]))
elif figure=='4':
    radius = int(input('enter the radius:'))
    perimetr = 2 * pi * radius

print('figure perimeter:', perimetr)