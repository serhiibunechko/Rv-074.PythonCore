#The YEAR is known. Determine whether this year is intercalary and to what century this year belongs
year = int(input('Enter a year:'))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")

century = (year - 1) // 100 + 1        
print('century:', century)