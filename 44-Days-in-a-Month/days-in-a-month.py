# Given the variable,

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# define a procedure, how_many_days,
# that takes as input a number
# representing a month, and returns
# the number of days in that month.

def how_many_days(month_number):
    if month_number == 1:
        return days_in_month[0]
    elif month_number == 2:
        return days_in_month[1]
    elif month_number == 3:
        return days_in_month[2]
    elif month_number == 4:
        return days_in_month[3]
    elif month_number == 5:
        return days_in_month[4]
    elif month_number == 6:
        return days_in_month[5]
    elif month_number == 7:
        return days_in_month[6]
    elif month_number == 8:
        return days_in_month[7]
    elif month_number == 9:
        return days_in_month[8]
    elif month_number == 10:
        return days_in_month[9]
    elif month_number == 11:
        return days_in_month[10]
    elif month_number == 12:
        return days_in_month[11]
    else:
        return -1
    

#print how_many_days(1)
#>>> 31

#print how_many_days(9)
#>>> 30
