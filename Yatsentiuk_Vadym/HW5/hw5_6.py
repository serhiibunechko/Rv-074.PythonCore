countPositive = 0
countNegative = 0
i = 1

while True:
    userNumber = int(input("Enter number: "))

    if userNumber == 0:
        print("Stops the program")
        break
    elif userNumber > 0:
        countPositive += 1

    else:
        countNegative += 1
    i += 1

percentPositive = (countPositive * 100) / (countPositive + countNegative)
percentNegative = (countNegative * 100) / (countPositive + countNegative)

print("Percentage of positive numbers: {}""\n""Percentage of negative numbers: {}".format(percentPositive,
                                                                                          percentNegative))
