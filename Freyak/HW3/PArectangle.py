width = float(input("Input width of rectangle "))
height = float(input("Input height of rectangle "))
choise = int(input("Select the action:\nPrint 1 for perimeter\nPrint 2 for area\n"))
if width <= 0 or height <=0:
    print("Incorrect input ")
else:
    if choise == 1:
        print("P = ", width*2 + height*2)
    if choise == 2:
        print("S = ", width*height)
    if choise < 1 or choise > 2:
        print("Incorrect input")
