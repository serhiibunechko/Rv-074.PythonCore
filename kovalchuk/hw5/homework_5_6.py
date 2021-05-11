xList = [int(x) for x in input("Enter list of numbers: ").split()]
positiveNum = 0
negativeNum = 0

for num in xList:
    if num == 0:
        print("Goodbye")
    elif num > 0:
        positiveNum+=1
    elif num < 0:
        negativeNum+=1
percentPositive = (positiveNum / len(xList)) * 100
percentNegative = (negativeNum / len(xList)) * 100
print("%.2f%% of values in list are positive"%percentPositive,"\n" "%.2f%% of values in list are negative"%percentNegative)