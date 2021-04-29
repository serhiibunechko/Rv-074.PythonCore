firstCh = str(input("input first character: "))[:1]
secCh = str(input("input second character: "))[:1]
for i in range(1, 7):
    if i == 1 or i == 6:
        print(firstCh*7)
    else:
        print(firstCh + secCh*5 + firstCh)
