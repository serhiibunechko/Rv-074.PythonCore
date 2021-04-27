y = int(input("Money:"))
if y % 200 == 0:
    c=y // 200
else:
    c=y // 200
    print ("200:", c)
a = 200 * c
b = y-a
if b % 100 == 0:
    n=b // 100
else:
    n=b // 100
    print ("100:", n)
d = 100 * n
f = b-d
if f % 100 == 0:
    v=f // 10
else:
    v=f //10
    print("10:", v)
x = 10 * v
z = f-x
if z % 100 ==0:
    m=z // 1
else:
    m=z // 1
    print("1:", m)