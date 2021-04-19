# encoding: utf-8

variables = {
        'first' : None,
        'second' : None
        }

for i in variables:
    successful = False

    while not successful:
        variables[i] = input(f'Please input {i} variable: ').strip()

        if variables[i].isdigit():
            variables[i] = int(variables[i])
            successful = True
        else:
            print(f'{i.capitalize()} variable must have a numeric value.')
            continue


print()
print(variables['first'], ' + ', variables['second'], ' = ', variables['first'] + variables['second'])
print(variables['first'], ' - ', variables['second'], ' = ', variables['first'] - variables['second'])
print(variables['first'], ' * ', variables['second'], ' = ', variables['first'] * variables['second'])
print(variables['first'], ' / ', variables['second'], ' = ', variables['first'] / variables['second'])

