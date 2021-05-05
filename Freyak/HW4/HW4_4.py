import math


while True:
    try:
        K = float(input("Input K(passage) "))

        if K <= 0:
            raise Exception

        S = float(input("Input S(hall area) "))

        if S <= 0:
            raise Exception

        R = float(input("Input R(radius of the stage) "))

        if R <= 0:
            raise Exception

        def option():

            if math.sqrt(S) - R * 2 > K:
                return 1
            else:
                return 2


        if option() == 1:
            print("Possible")

        if option() == 2:
            print("Impossible")

        break

    except ValueError:
        print("Value Error")
    except Exception:
        print("K,S,R should be>0")
