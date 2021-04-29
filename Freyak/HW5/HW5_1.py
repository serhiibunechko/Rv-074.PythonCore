var = int(input())
const = 34
attempt = 0
while attempt < 9:

    while var != const:
        if attempt < 9:
            if var > const:
                print("Your input is > then var")
                var = int(input())
            elif var < const:
                print("your input is < than var")
                var = int(input())
        attempt += 1
        if attempt > 9:
            print("Sorry you lose")
            break
    if var == const:
        print("You won")
        break
