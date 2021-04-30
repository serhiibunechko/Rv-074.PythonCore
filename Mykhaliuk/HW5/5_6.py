#For user-entered numbers, determine the percentage of
#positive and negative numbers. 
#When entering the number 0, finish the job.​
summ = negative = positive = 0
while True:
    number = int(input("Enter a number: "))
    if number < 0:negative += abs(number)
    elif number > 0:positive += number 
    elif number == 0:break
    summ += abs(number)
    print(f"{positive*100/summ:.1f}% of positive numbers")
    print(f"{negative*100/summ:.1f}% of negative numbers")