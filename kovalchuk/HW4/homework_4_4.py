import math 
r = float(input("Radius of stage: "))
s = float(input("Area of Square: "))
k = float(input("Enter the min distance: "))
if (math.sqrt(s) - 2*r) < k:
    print("Small Distance")
elif (math.sqrt(s) - 2*r) >= k:
    print("Distance is normal")
else:
    print("The data is incorrect") 