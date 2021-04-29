cont = 0
var = 0
while cont < 10:
    a = int(input("Input a: "))
    if a % 5 == 0:
        var += 1
    cont += 1
print(var)
