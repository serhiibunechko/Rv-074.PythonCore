numbers = []
count = 0

for i in range(1, 11):
    enterValue = int(input('Enter number {}: '.format(i)))
    if enterValue % 5 == 0:
        numbers.append(enterValue)
        count += 1

print("{}, The number of numbers divisible by 5: {}".format(numbers, count))
