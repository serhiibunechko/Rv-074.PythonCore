maxNumber = 10

for row in range(1, maxNumber):
    for column in range(1, maxNumber):
        print(row*column, end='\t')
    print()
