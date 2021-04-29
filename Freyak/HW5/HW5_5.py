P = 34
H = 56
suma = 0
mult = 1
count = 0
while True:
    try:
        a = int(input())
        if a == int(P) or a == int(H):
            break
        if a < P:
            suma += a
        if a > H:
            mult *= a
        if P < a < H:
            count += 1
    except ValueError:
        print("Value error")
print("The sum of numbers that are less than P = ", suma)
print("Product of numbers greater than H = ", mult)
print("the number of numbers in the range of values from P to H =", count)
