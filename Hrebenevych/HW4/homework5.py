# encoding: utf-8

import sys


amount_money = input('Enter a amount of money: ').strip()

if amount_money.isdigit() or '.' in amount_money \
                        and amount_money.count('.') == 1 \
                        and amount_money[0] != '.' \
                        and amount_money[-1] != '.':
    amount_money = float(amount_money)
else:
   print("\nThe amount of money can include only numbers and '.'\nExample: 12, 16.5")
   sys.exit()

if amount_money:
    two_hundred = amount_money // 200
    print('200: {}'.format(two_hundred))

amount_money -= two_hundred * 200

if amount_money:
    one_hundred = amount_money // 100
    print('100: {}'.format(one_hundred))

amount_money -= one_hundred * 100

if amount_money:
    ten = amount_money // 10
    print('10:  {}'.format(ten))

amount_money -= ten * 10

if amount_money:
    one = amount_money // 1
    print('1:   {}'.format(one))

