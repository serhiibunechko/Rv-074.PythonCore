digit = int(input("Enter value: "))

if digit > 0:
    print("This is a positive number, it's length", len(str(digit)), "characters")
elif digit < 0:
    print("This is a negative number, it's length", str(len(str(digit)) -1), "characters")
else:
    print("This number is 0, its length is 1 character")