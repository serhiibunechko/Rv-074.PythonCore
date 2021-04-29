# encoding: utf-8

"""I try resolve this task without using loops or [try:except:] statements.
"""

import math
import sys


userRequest = """
Enter a number operation:
    Calculate square of rectangle       [1]:
    Calculate square of right triangle  [2]:
    Calculate square of circle          [3]:
Option: """

userChoice = input(userRequest).strip()
print()

if userChoice not in ['1','2','3']:
    print("You're choice not correct. Operation must be 1 or 2 or 3.")
    sys.exit()

if userChoice == '1':

    firstside = input('enter the value first side of the rectangle: ').strip()
    secondside = input('enter the value second side of the rectangle: ').strip()

    if firstside.isdigit() or '.' in firstside \
                            and firstside.count('.') == 1 \
                            and firstside[0] != '.' \
                            and firstside[-1] != '.':
        firstside = float(firstside)
    else:
        print("\nfirst side value can include only numbers and '.'\nexample: 12, 16.5")
        sys.exit()


    if secondside.isdigit() or '.' in secondside \
                            and secondside.count('.') == 1 \
                            and secondside[0] != '.' \
                            and secondside[-1] != '.':
        secondside = float(secondside)
    else:
        print("\nSecond side value can include only numbers and '.'\nexample: 12, 16.5")
        sys.exit()

    print("Square of rectangle: {}".format(firstSide * secondSide))

elif userChoice == '2':

    firstside = input('Enter the value first side of the triagle: ').strip()
    secondside = input('Enter the value second side of the triagle: ').strip()

    if firstside.isdigit() or '.' in firstside \
                            and firstside.count('.') == 1 \
                            and firstside[0] != '.' \
                            and firstside[-1] != '.':
        firstside = float(firstside)
    else:
        print("\nFirst side value can include only numbers and '.'\nExample: 12, 16.5")
        sys.exit()


    if secondside.isdigit() or '.' in secondside \
                            and secondside.count('.') == 1 \
                            and secondside[0] != '.' \
                            and secondside[-1] != '.':
        secondside = float(secondside)
    else:
        print("\nSecond side value can include only numbers and '.'\nExample: 12, 16.5")
        sys.exit()

    print("Area of right triagle: {}".format((firstside * secondside) / 2))

else:

    circleRadius = input("Enter the radius of circle: ").strip()

    if circleRadius.isdigit() or '.' in circleRadius \
                            and circleRadius.count('.') == 1 \
                            and circleRadius[0] != '.' \
                            and circleRadius[-1] != '.':
        circleRadius = float(circleRadius)
    else:
        print("\nRadius value can include only numbers and '.'\nExample: 12, 16.5")
        sys.exit()

    print("Area of circle: {}".format(math.pi * circleRadius**2))

