from math import sqrt
FirKatet = float(input("Input length of first Katet:  "))
SecKatet = float(input("Input length of second Katet: "))
if FirKatet <= 0 or SecKatet <= 0:
    print("Incorrect input")
else:
    print("Hypotenuse = ", sqrt(FirKatet**2+SecKatet**2))