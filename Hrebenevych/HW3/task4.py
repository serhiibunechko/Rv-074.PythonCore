# encoding: utf-8

import math


print('Simple program for calculating area and perimeter the circle')

variables = {
        'radius': None,
        }

for i in variables:
    successfull = False

    while not successfull:
        variables[i] = input(f'Enter the {i} of circle: ').strip()

        try:
            variables[i] = float(variables[i])
            successfull = True
        except:
            print(f"{i.capitalize()} must have a integer or float value. Delimiter is '.'")
            continue

print(f"Perimeter of circle is: {round(2 * math.pi * variables['radius'], 3)}")
print(f"Area of circle is: {round(math.pi * variables['radius']**2, 3)}")

