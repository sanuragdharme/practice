# To check whether the entered year is Leap year or not


def check_leap_year(year):
    if not year.isdigit():
        print("Please enter year in numeric format (YYYY).")
        return

    year = int(year)

    if len(str(year)) < 4:
        print("Length of year should be 4.")
        return

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("{} is a leap year.".format(year))
            else:
                print("{} is not a leap year.".format(year))
        print("{} is a leap year.".format(year))
    else:
        print("{} is not a leap year.".format(year))


check_leap_year(input("Enter Year: "))
