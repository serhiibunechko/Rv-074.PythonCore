# encoding: utf-8

import math

print('Simple program for calculating area the length of the hypotenuse.')


variables = {
        'first': None,
        'two': None
        }

for i in variables:
    successfull = False

    while not successfull:
        variables[i] = input(f'Enter the {i} side of the right triangle: ').strip()

        try:
            variables[i] = float(variables[i])
            successfull = True
        except:
            print("Value must have a integer or float value. Delimiter is '.'")
            continue


print(f"The length of the hypotenuse is: {round(math.sqrt(variables['first']**2 + variables['two']**2), 3)}")

