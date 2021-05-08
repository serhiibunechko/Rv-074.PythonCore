import random

length = int(input("Plz enter how much of variables do you want to enter: "))
FirList = []
SecList = list(map(int, input(f"Plz enter {length} numbers: ").strip().split()))[:5]
ThirdList = []

for i in range(0, length):

    n = random.randint(0, 100)
    FirList.append(n)

for i in range(0, length):
    ThirdList.append(FirList[i]+SecList[i])

print("Randomly created: ", FirList)
print("Your list: ", SecList)
print("Sum list: ", ThirdList)
