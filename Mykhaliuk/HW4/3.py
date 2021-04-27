#The user enters a number, the program must display its description.
#For example, "positive one-digit", "negative two-digit", etc.
number = input('Enter a number:')

number_of_didgits = len(number)
positivity = 'positive'

if int(number) < 0:
    positivity = 'negative'
    number_of_didgits -= 1
    print("you've entered", positivity, number_of_didgits, '- didgit number')
elif number == '0':
    print("you've entered zero")    
else:
    print("you've entered", positivity, number_of_didgits, '- didgit number')