# encoding: utf-8

import sys


squareHall = input('Please enter an area of a square hall:: ').strip()
sceneRadius = input('Enter a radius of scene: ').strip()
passageLength = input('Enter a passage value from the wall to the scene: ').strip()

if squareHall.isdigit() or '.' in squareHall \
                        and squareHall.count('.') == 1 \
                        and squareHall[0] != '.' \
                        and squareHall[-1] != '.':
    squareHall = float(squareHall)
else:
   print("\nArea of square hall value can include only numbers and '.'\nExample: 12, 16.5")
   sys.exit()


if sceneRadius.isdigit() or '.' in sceneRadius \
                        and sceneRadius.count('.') == 1 \
                        and sceneRadius[0] != '.' \
                        and sceneRadius[-1] != '.':
   sceneRadius = float(sceneRadius)
else:
   print("\nScene radius value can include only numbers and '.'\nExample: 12, 16.5")
   sys.exit()


if passageLength.isdigit() or '.' in passageLength \
                        and passageLength.count('.') == 1 \
                        and passageLength[0] != '.' \
                        and passageLength[-1] != '.':
   passageLength = float(passageLength)
else:
   print("\nPassage length value can include only numbers and '.'\nExample: 12, 16.5")
   sys.exit()


oneSideHallLength = round(squareHall**0.5, 2)
sceneDiameter = sceneRadius * 2

if oneSideHallLength - sceneDiameter < passageLength:
    print('Not possible to place a round stage in the square hall with a passage  {}'.format(passageLength))
else:
    print('Possible to place a round stage in the square hall with a passage {}'.format(passageLength))

