import math

print("Input lengths of other triangle sides:")
a = float(input("a: "))
b = float(input("b: "))

c = math.sqrt(a**2 + b**2)
print("The length of the hypotenuse is {0:.3f}".format(c))
