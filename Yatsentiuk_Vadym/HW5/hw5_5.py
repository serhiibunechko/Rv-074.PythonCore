p = int(input("Enter P: "))
h = int(input("Enter H: "))
sumUserNumber = 0
multiUserNumber = 1
i = 1

while True:
    userNumber = int(input("Enter number: "))

    if userNumber == p or userNumber == h:
        print("Stops the program")
        break
    elif userNumber < p:
        sumUserNumber += userNumber
    elif userNumber > h:
        multiUserNumber *= userNumber
    else:
        print("We don't use this range")
    i += 1

print("Sum all: {}""\n""Multi all: {}""\n""Range from P to H: {}".format(sumUserNumber, multiUserNumber, (h-p)))
