# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#
#procedure to check whether year is leap or not
def isLeapYear(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

#procedure to determine days in month
def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7\
    or month == 8 or month == 10 or month == 12:
        return 31
    elif month == 2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
        return 30

#procedure to determine next day to the given date
def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    if month == 12:
        return year + 1, 1, 1
    else:
        return year, month + 1, 1

#procedure to check date1 is before date2 or not , if date1 is before 
#date2 it returns True otherwise False
def isBeforeDate(year1, month1, day1, year2, month2, day2):
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        else:
            return day1 < day2
    return False

#procedure to calculate days between two given dates
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    assert isBeforeDate(year1, month1, day1, year2, month2, day2)
    
    days = 0
    while isBeforeDate(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days = days + 1
    return days 
    
    
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
