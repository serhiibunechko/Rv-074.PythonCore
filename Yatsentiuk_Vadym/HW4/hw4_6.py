number_of_place = int(input("Enter number: "))

if number_of_place > 36 and number_of_place % 2 == 0 and number_of_place <= 54:
    print("Your place on top, on the side")
elif number_of_place > 36 and number_of_place % 2 != 0 and number_of_place <= 54:
    print("Your place on bottom, on the side")
elif 1 <= number_of_place <= 36 and number_of_place % 2 != 0:
    print("Your place on bottom, on the compartment")
else:
    print("Your place on top, on the compartment")