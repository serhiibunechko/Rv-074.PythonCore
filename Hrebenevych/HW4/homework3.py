# encoding: utf-8

import sys


userNumber = input('Enter positive or negative number: ').strip()

if userNumber[0] == '-' or userNumber.isdigit():
    numberLength = len(userNumber)
    userNumber = int(userNumber)

    if userNumber > 0:
        print("Positive {} digits number.".format(numberLength))
    elif userNumber < 0:
        # in this case '1' it's '-' symbol for negative number
        print("Negative {} digits number.".format(numberLength - 1))
    else:
        print('Number is zero.')
else:
    print('A number contains not the only digits.')

