#check distance from line of stage to line of square hall
import math
squareHall = int(input("Enter square of Hall: "))
squareStage = int(input('Enter square of Stage: '))
passageLength = int(input('Enter length of Passage: '))

if passageLength == 0:
    print('No Possible')
elif passageLength <= (math.sqrt(squareHall)) - (squareStage / math.pi):
    print('Its possible')
else:
    print('Its no possible')