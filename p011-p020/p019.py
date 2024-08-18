# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September, April, June and November.
# All the rest have thirty-one, Saving February alone, Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def count_days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 29
        else:
            return 28

def count_first_sundays(year):  # from 1 Jan 1901 to 31 Dec (year - 1)
    count = 0
    days = 0
    for y in range(1900, year):
        for m in range(1, 13):
            if days % 7 == 6:
                count += 1
            days += count_days(m, y)
    return count

ans = count_first_sundays(2001) - count_first_sundays(1901)
print(ans)