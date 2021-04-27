import math
choise = input("Rectangle\n Triangle\n Circle")
if choise == "Rectangle":
    width = float(input("Width: "))
    height = float(input("Height: "))
    area = width * height
    print("Area of Rectangle=", area)
elif choise == "Triangle":
    a = float(input("First side: "))
    b = float(input("Second side: "))
    c = float(input("Third side: "))
    area = a+b+c
    print("Area of Triangle=", area)
elif choise == "Circle" :
    radius = float(input("Radius?"))
    area = math.pi * radius**2
    print("Area of Circle=", area)
else :
    print("Make a choise")