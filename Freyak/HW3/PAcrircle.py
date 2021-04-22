import math
radius = float(input("Input radius of circle "))
choise = int(input("Select the action:\nPrint 1 for perimeter\nPrint 2 for area\n"))
if choise == 1:
    print("P = ", 2*math.pi*radius)
if choise == 2:
    print("S = ", radius**2*math.pi)
if choise < 1 or choise > 2:
    print("Incorrect input")

