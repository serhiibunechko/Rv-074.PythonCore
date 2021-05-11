xList = [int(x) for x in input('Enter list of numbers: ').split()]
count = 0


for num in xList:
    if num % 5 == 0:
        count+=1
print(count, "numbers that are multiples of 5")