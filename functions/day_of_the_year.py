def is_year_leap(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    if month == 1 or month == 3 or month ==  5 \
    	or month ==  7 or month ==  8 \
    	or month ==  10 or month == 12:
        return 31
    if month ==  4 or month ==  6 \
    	or month ==  9 or month == 11:
        return 30

def day_of_year(year, month, day):
    feb = 28 
    if is_year_leap(year):
        feb = 29
    if month > 2:
        total = 31 + feb
        month = month - 3
        i = 0
        while month > 0:
            if month % 2 != 0:
                total = total + 31
            else:
                total = total + 30
            month = month - 1
        total = total + day
    return total
print(day_of_year(2000, 10, 29))