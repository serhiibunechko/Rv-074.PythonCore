# encoding: utf-8

print('Simple program for calculating area and perimeter the rectangle')


variables = {
        'width': None,
        'height': None
        }

for i in variables:
    successfull = False

    while not successfull:
        variables[i] = input(f'Enter the {i} of rectangle: ').strip()

        try:
            variables[i] = float(variables[i])
            successfull = True
        except:
            print(f"{i.capitalize()} must have a integer or float value. Delimiter is '.'")
            continue


print(f"Perimeter od rectangle is: {2 * (variables['height'] + variables['width'])}")
print(f"Area of rectangle is: {variables['height'] * variables['width']}")

