mainList = list(map(str, input(f"Plz enter smt: ").strip().split()))[:5]
numList = []
letList = []
trashList = []

for i in range(0, len(mainList)):
    a = mainList[i]

    if a.isdigit() or a[0] == f'-{a.isdigit()}':
        numList.append(mainList[i])

    elif a.isalpha():
        letList.append(mainList[i])

    else:
        trashList.append((mainList[i]))

print("List of numbers: ", numList)
print("List of letters: ", letList)
print("List of trash: ", trashList)
