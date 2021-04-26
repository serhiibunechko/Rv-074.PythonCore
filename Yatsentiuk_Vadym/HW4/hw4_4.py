from math import sqrt


circle_radius = int(input("Enter radius: "))
square = int(input("Enter square: "))
k = int(input("Enter the min distance: "))

if (sqrt(square) - 2*circle_radius) < k:
    print("The passage is too small")
elif (sqrt(square) - 2*circle_radius) >= k:
    print("The distance is normal")
else:
    print("The data is incorrect")