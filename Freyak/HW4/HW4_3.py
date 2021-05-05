try:
    value = int(input("Input your integer number "))

    if value > 0:
        print(f"Число додатнє, {len(str(value))} - значне")

    elif value < 0:
        print(f'Число відємне, {len(str(value)) - 1} - значне')

    else:
        print("Your number is 0, it is non positive and non negative")
except ValueError:
    print("Value error")
