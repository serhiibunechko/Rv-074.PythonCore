money = int(input("How money do you have: "))
twoHundred = money//200
oneHundred = (money - twoHundred*200)//100
tenUAH = (money - twoHundred*200 - oneHundred*100)//10
oneUAH = (money - twoHundred*200 - oneHundred*100-tenUAH*10)//1

cash = {twoHundred: "200UAH", oneHundred: "100UAH", tenUAH: "10UAH", oneUAH: "1UAH"}
for i in cash:
    if i > 0:
        print(i, cash[i])
