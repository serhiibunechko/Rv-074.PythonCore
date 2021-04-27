n = int(input("Number of a place: "))
if n == 1 or 3 or 5 or 7 or 9 or 11 or 13 or 15 or 17 or 19 or 21 or 23 or 25 or 27 or 29 or 31 or 33 or 35:
    print("Your place in the bottom of compartment")
elif n == 2 or 4 or 6 or 8 or 10 or 12 or 14 or 16 or 18 or 20 or 22 or 24 or 26 or 28 or 30 or 32 or 34 or 36:
    print("Your place in the top of compartment")
elif n == 37 or 39 or 41 or 43 or 45 or 47 or 49 or 51 or 53:
    print("Your place in the bottom of side")
elif n == 38 or 40 or 42 or 44 or 46 or 48 or 50 or 52 or 54 or 56:
    print("Your place in the top of side")
else:
    print("Incorrect number")