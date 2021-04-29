# encoding: utf-8

import sys


variables = {
        'capacity': None,
        'amount': None
        }

for i in variables:
    successfull = False

    while not successfull:
        variables[i] = input(f'Enter a fuel {i} in a tank: ').strip()

        try:
            variables[i] = float(variables[i])
            successfull = True
        except:
            print(f"{i.capitalize()} must have a integer or float value. Delimiter is '.'")
            continue


if variables['amount'] > variables['capacity']:
    print('The amount of fuel cannot exceed the fuel supply.')
    sys.exit()

currentFuelPercent = round(variables['amount'] / variables['capacity'], 2)

sensor = 'Green'

if currentFuelPercent <= 0.1:
    sensor = 'Red'

print(f'Sensor: {sensor}')

