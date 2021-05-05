while True:
    try:
        year = int(input("Input year, you want to check: "))
        if year != int(year):
            raise Exception
        break
    except Exception:
        print('Incorrect value ')
while True:
    try:
        choice = int(input("Press 1 to check if year is leap year\nPress 2 to know century\n"))
        if choice < 1 or choice > 2:
            raise Exception
        if choice == 1:
            def LeapYearCheck(year):
                return ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)


            if LeapYearCheck(year):
                print(f"Year {year} is leap Year")
            else:
                print(f"Year {year} isn't a Leap Year")
        if choice == 2:
            century = int(year / 100 + 1)
            print(century)
        break
    except ValueError:
        print('Incorrect value type')
    except Exception:
        print('Please enter value 1 or 2')
