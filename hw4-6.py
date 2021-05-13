#check what place in train

place = int(input('Enter your place: '))
topOrBottom = place
DepartmentOrside = place

if topOrBottom % 2 == 0:
    print('Parne')
else:
    print('Neparne')
if DepartmentOrside <= 38:
    print('Department')
else:
    print('Side')
