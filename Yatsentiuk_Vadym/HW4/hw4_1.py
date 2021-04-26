year = int(input("Enter year: "))

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print(year, 'leap year')
    if year % 100 == 0:
        сentury = year // 100
    else:
        century = year // 100+1
    print("It's",century,"century")
else:
    print("This year is not leap")