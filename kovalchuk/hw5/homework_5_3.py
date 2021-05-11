number = int(input("Print number you want multiply: "))

for x in range(1,10):
    print(number, "*", x, "=", number*x)


for x in range(1,10):
    for y in range(1,10):
        print(x, "*", y, "=", x*y)