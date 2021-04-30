#Given the number P and the number H.
#The user enters a sequence of numbers.
#Determine: the sum of those numbers that are less than P;
#product of numbers greater than H;
#the number of numbers in the range of values ​​from P to H.
#When entering a number equal to P or H,
#stop the calculation and display the result.
from random import randrange


p = randrange(30)
h = randrange(30)
lessThanPsum = amountInRange = 0
graterThanHprod = 1
while True:
    n = int(input('Enter random number(from 0 to 30):'))
    if n == p or n ==h:break
    if n < p:lessThanPsum += n
    if n > h:graterThanHprod *= n
    if p<h and p<n<h or p>n>h and p>h :amountInRange += 1
print('Resault: P =', p, 'H =', h,
      '\nThe sum of numbers that are less than P:', lessThanPsum,
      '\nProduct of numbers that are greater than H:', graterThanHprod,
      '\nAmount of numbers in the P to H range:', amountInRange)