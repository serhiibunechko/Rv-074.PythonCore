import numpy as np

leng = int(input("How many rows and cols matrix should have?: "))
mainList = np.random.randint(100, size=(leng, leng))
secList = []

print(f'Our matrix:\n {mainList}\n\n')

for i in range(0, leng):
    colMin = 0
    for j in range(0, leng):
        colMin = min(mainList[i])
    secList.append(colMin)
print("The maximum element among the minimum elements of the matrix columns is: ", max(secList))
