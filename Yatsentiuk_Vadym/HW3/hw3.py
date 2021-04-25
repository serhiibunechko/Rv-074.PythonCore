# task 1

a = 1
b = 2
a, b = b, a
print(a)
print(b)


# task 2

num_bytes = float(input("Enter number: "))

kilobytes = num_bytes / 1000
megabytes = kilobytes / 1024

print("In ",num_bytes,"bytes""\n" + str(kilobytes),"kilobytes""\n" + str(megabytes),"megabytes")


# task 3

height_rect = int(input("Enter height: "))
width_rect = int(input("Enter width: "))

print("Perimetr of the rectangle: " + str(2*height_rect + 2*width_rect))
print("Area of the rectangle: " + str(height_rect*width_rect))


#task 4

circle_radius = int(input("Enter radius: "))

circle_perimetr = 2 * 3.14 * circle_radius
circle_area = 3.14 * circle_radius**2

print("Perimetr: " + str(circle_perimetr) + "\n" + "Area: " + str(circle_area))

# task 5

side_first = int(input("Enter first side: "))
side_second = int(input("Enter second side: "))

print("The hypotenuse is equal to: " + str(side_first**2 + side_second**2))