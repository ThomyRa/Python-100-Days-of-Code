# # Formating a name challenge

# def format_name(f_name, l_name):
#     fullname = f_name + ' ' + l_name
#     return fullname

# print(format_name("Bob", "Joe"))

# Leap year function
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

# print ("Is leap" if is_leap(year) else "Is not leap")

def days_in_month(year_eval, month_eval):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year_eval):
        if month_eval == 2:
            return 29
        else:
            return month_days[month_eval - 1]
    else:
        return month_days[month_eval - 1]

year = int(input("Insert a year: "))
month = int(input("Insert a month: "))
days = days_in_month(year, month)
print(days)
