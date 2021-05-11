import random

print ("HELLO!\n You have 10 tries to guess the correct number!")
number = random.randint(0,101)
guess = int(input("Guess the number: "))
tries = 1

if number == guess:
    print("Nice answer")
elif guess < 0 or guess > 101:
    print("Try again")
while tries < 10 and number > int(guess):
    guess = input("The hidden number is bigger, try again: ")
    tries += 1
while tries < 10 and number < int(guess):
    guess = input("The hidden number is less, try again: ")
    tries += 1
if tries == 10:
    print("You lost!")
elif number == int(guess):
    print("You Win!")