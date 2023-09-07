def detect_leap_year(year):
    is_leap_year = year % 4 == 0

    if is_leap_year:
        return True
    else:
        return False


def days_in_month(month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    thirty_days = 30
    twenty_eight_day = 28
    for day in month_days:
        print(day)

days_in_month()
