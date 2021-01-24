

import datetime
import calendar

# Both datetime and calendar has weekday() method to obtain the index of week of day based on
#   year, month, day

day_of_weeks = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

def soln1():
    month, day, year = map(int, input().split() )
    print( day_of_weeks[ datetime.date(year, month, day).weekday() ] )


def soln2():
    month, day, year = map(int, input().split())
    print( day_of_weeks[ calendar.weekday(year, month, day) ] )