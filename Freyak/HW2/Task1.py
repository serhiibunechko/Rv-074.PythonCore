try:
    a = float(input("Input variable A: "))
except ValueError:
    print("Type error, try again")
    exit()
try:
    b = float(input("Input variable B: "))
except ValueError:
    print("Type error, try again")
    exit()
try:
    opt = float(
        input("If you want to do all 4 actions, press 1\nIf you want to choose what action to do, press 2\nPress: "))
except ValueError:
    print("Type error, first option initialized")
    opt = 1

try:
    if opt > 2:
        print("Incorrect value")
except Exception:
    print("This input is invalid.")

if opt == 1:
    print("a + b = ", a + b)
    print("a - b = ", a - b)
    try:
        a / b
    except ZeroDivisionError:
        print("Zero division error")
    else:
        print("a / b = ", a / b)
    print("a * b = ", a * b)
if opt == 2:
    action = input("Input action you want to do (+ - / *): ")
    if action == "+":
        print("a + b = ", a + b)
    if action == "/":
        try:
            a / b
        except ZeroDivisionError:
            print("Zero division error")
        else:
            print("a / b = ", a / b)
    if action == "-":
        print("a - b = ", a - b)
    if action == "*":
        print("a * b = ", a * b)
    else:
        print("Incorrect input")
