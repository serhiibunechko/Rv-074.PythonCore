figure = input("What do you choose: rectangle, triangle or circle? ")

if figure == "rectangle":
    first_side_rectangle = int(input("Enter the first side: "))
    second_side_rectangle = int(input("Enter the second side: "))
    print("The area of ​​the rectangle:", str(first_side_rectangle*second_side_rectangle))
elif figure == "triangle":
    side_triangle = int(input("Enter the first side: "))
    height_triangle = int(input("Enter the height triangle: "))
    print("The area of ​​the triangle:", str((side_triangle*height_triangle)//2))
elif figure == "circle":
    circle_radius = int(input("Enter the radius: "))
    print("The area of ​​the circle:", str(3.14 * circle_radius**2))
else:
    print("False data")