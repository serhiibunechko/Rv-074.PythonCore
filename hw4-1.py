#check leap year or not and what century of
year = int(input('Введіть рік : '))
if (year % 4) == 0 and (year % 100) == 0 or (year % 400) == 0:
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
century = year // 100
if year % 100 != 0:
    century = century + 1
    print(century)
