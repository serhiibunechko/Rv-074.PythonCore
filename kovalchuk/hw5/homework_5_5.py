P = int(input("Number 1: "))
H = int(input("Number 2: "))
xList = [int(x) for x in input("Sequence of numbers: ").split()]
lessThanP = 0
higherThanH = 0
PHrange = 0

for num1 in xList:
    while num1 == P or H:
        break
    if num1 < P:
        lessThanP += num1
    elif num1 > H:
        higherThanH += num1
    elif num1 > P or num1 < H:
        PHrange += num1
    

print("sumlessThanP", lessThanP,"\n""sumhigherThanH", higherThanH,"\n""sumPHrange", PHrange)