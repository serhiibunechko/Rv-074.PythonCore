#The program generates a random integer from 0 to 100.
#The user must guess it in no more than 10 attempts. 
#After each unsuccessful attempt, program says if the number,
#entered by user more or less than required number. 
#If the number is not guessed for 10 attempts, then display the guessed number.
from random import randrange


number = randrange(100)
attempt = 0

while True:
    if attempt > 9:
            print("You didn't manage to guess a number in 10 attempts!")
            break

    guess = int(input('Guess a number(from 0 to 100):'))
    print(f'attempt #{attempt+1}:', end = '')
    if guess < number: print('your guess is smaller than the number')
    elif guess > number :print('your guess is higher than the number')            
    else: 
        print('you won in', attempt+1, 'attempt(s)!')
        break
    attempt += 1
