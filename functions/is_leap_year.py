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

test_years = [1900, 2000, 2016, 1987, 1900, 2000, 2016, 1987, 1900, 2000, 2016, 1987]
test_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
test_results = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")
