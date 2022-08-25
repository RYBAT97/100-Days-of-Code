# def format_name(f_name, l_name):
#     return f_name.title(), l_name.title()
#
#
# a, b = format_name("ali", "rezaei")
# print(f"{a} {b}")

# ----------------------------------------------------

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """Returns number of days in a month. It takes the year as input too
    so if it is a leap year, February would have 29 days"""
    is_it_leap = is_leap(year)
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_it_leap and month == 2:
        return month_days[1] + 1
    else:
        return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
