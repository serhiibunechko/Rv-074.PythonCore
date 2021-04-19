
choice = input("Choice operration:\n1. +\n2. -\n3. *\n4. /\n")

a = int(input("Enter a:"))
b = int(input("Enter b:"))

if(choice == "1"):
    c = a+b
    print (a, "+", b, "=", c)
elif(choice == "2"):
    c = a-b
    print (a, "-", b, "=", c)
elif(choice == "3"):
    c = a*b
    print (a, "*", b, "=", c)
elif(choice == "4"):
    c = a/b
    print (a, "/", b, "=", c)
else:
    print("Error choice")