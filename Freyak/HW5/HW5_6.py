cont = 0
var1 = 0
var2 = 0

while True:
    try:
        a = int(input("Input a: "))
        if a > 0:
            var1 += 1
        if a < 0:
            var2 += 1
        if a == 0:
            break
        cont += 1
    except ValueError:
        print("Value error")

print(f"{var1*100/cont}% of positive")
print(f"{var2*100/cont}% of negative")
