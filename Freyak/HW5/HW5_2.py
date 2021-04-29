cont = 0
var = list(map(int, input("Enter 10 integer elements without ','(more than 10 numbers are unavailable): ").strip().split()))[:10]
#var = []
#for i in range(1, 11):
#    a = int(input())
#    var += [a]
#    i+=1
#print(var)
choose = int(input(
    "If you want to see how many variables multiples of 5 press 1:\n"
    "If you want to see WHAT numbers multiples of 5 press 2:\n"))
new = []

if choose == 1:
    for i in var:
        if i % 5 == 0:
            cont += 1
    print(f"{cont} variables multiples of 5 ")
if choose == 2:
    for i in var:
        if i % 5 == 0:
            new += [i]
    print(f"{new}")
