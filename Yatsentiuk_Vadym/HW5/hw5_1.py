import random


guessesTaken = 0
guesses = random.randint(0, 101)

while guessesTaken <= 10:
    number = int(input("Enter number: "))
    guessesTaken += 1

    if guesses == number:
        print("Congrast! You guessed it.")
        break
    if guesses < number:
        print("Not enough")
    if guesses > number:
        print("Too much")
else:
    print("Did not guess.")