# encoding: utf-8

while True:
    year = input('Enter a year: ').strip()

    if year.isdigit():
        year = int(year)
        break
    else:
        continue

if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('{} it\'s a leap year.'.format(year))
else:
    print("{} isn't a leap year.".format(year))

century = year // 100 + 1

print("{} year it's {} century.".format(year, century))

