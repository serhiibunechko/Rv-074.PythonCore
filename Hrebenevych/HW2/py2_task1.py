# encoding: utf-8

while True:
    var_a = raw_input('Please enter a numerical value for first variable: ').strip()
    var_b = raw_input('Please enter a numerical value for second variable: ').strip()

    if var_a.isdigit():
        var_a = int(var_a)
    else:
        print('First variable must have numeric value!')
        continue

    if var_b.isdigit():
        var_b = int(var_b)
    else:
        print('Second variable must have numeric value!')
        continue

    if type(var_a) is int and type(var_b) is int:
        break


print
print var_a, ' + ', var_b, ' = ', var_a + var_b
print var_a, ' - ', var_b, ' = ', var_a - var_b
print var_a, ' * ', var_b, ' = ', var_a * var_b
print var_a, ' / ', var_b, ' = ', var_a / var_b

