amount = int(input("Enter amount: "))

if amount%200 == 0:
    print(str(amount//200), "banknotes")
elif amount%200 != 0 and amount%100 == 0:
    print(str(amount//200 + (amount%200 // 100)), "banknotes")
elif amount%100 != 0 and amount%10 == 0:
    print(str(amount//200 + (amount%200 // 100) + (amount%100 // 10)), "banknotes")
elif amount%10 != 0:
    print(str((amount//200 + (amount%200 // 100) + (amount%100 // 10)) + amount%10), "banknotes")
else:
    print("The data is incorrect")