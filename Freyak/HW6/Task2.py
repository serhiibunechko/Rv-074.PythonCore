import numpy as np

leng = int(input("How many rows and cols matrix should have?: "))
a = np.random.randint(100, size=(leng, leng))


print(f'Our matrix:\n {a}\n\n')

for i in range(0, leng):
    sumRow = 0
    for j in range(0, leng):
        sumRow = sumRow + a[i][j]
    print("Sum of " + str(i + 1) + " row: " + str(sumRow))


for i in range(0, leng):
    sumCol = 0
    for j in range(0, leng):
        sumCol = sumCol + a[j][i]
    print("Sum of " + str(i + 1) + " column: " + str(sumCol))
