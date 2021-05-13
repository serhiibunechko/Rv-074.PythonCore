#R - rectangle, T - triangle, C - circle
import math

square = input("The area of which to calculate: (r) or (t) or (c): ")
if square == 'r':
    width = float(input("Enter the width : "))
    height = float(input("Enter the height : "))
    square = width * height
    print("Area of Rectangle : {0:.2f}".format(square))
elif square == 't':
    base = float(input("Enter the length of base : "))
    height = float(input("Enter the height : "))
    square = 0.5 * base * height
    print("Area of Triangle : {0:.2f}".format(square))
elif square == 'c':
    radius = float(input("Enter the value of radius : "))
    square = math.pi * radius**2
    print("Area of Circle : {0:.3f}".format(square))