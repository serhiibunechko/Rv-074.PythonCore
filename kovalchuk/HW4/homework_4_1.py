y = int(input("Print year:"))
if y % 4 == 0 and y % 100 != 0:
    print("YES")
elif y % 400 == 0:
    print("YES")
else:
    print("NO")
if y % 100 == 0:
    c=y // 100
else:
    c=y // 100 + 1
print ("Century", c)