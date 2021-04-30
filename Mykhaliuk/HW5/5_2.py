#User enters ten natural numbers greater than 2.
#Count how many of them are numbers that are multiples of 5. 
numbers = (input("Enter 10 nuteral numbers grater than 2: ").split())
counter = i = 0
while i<10:
    if int(numbers[i]) % 5 == 0: counter += 1
    i += 1
print('You entered', counter, 'number(s) that are multiples of 5')