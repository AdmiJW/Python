

# In Julian calendar, leap year is checked simply by modulo 4.
#   If leap year, is 12th Sep, else 13th Sep

# On year 1918, the 256th day falls on 26th Sep

# In Gregorian calendar, leap year is checked if year divisible by 400, or divisible by 4 and not divisible by 100
#   Same, if leap then 12th Sep, else 13th Sep

def dayOfProgrammer(year):
    if year <= 1917:
        return f'13.09.{year}' if year % 4 else f'12.09.{year}'
    if year == 1918:
        return '26.09.1918'
    return f'12.09.{year}' if not (year % 400) or (year % 4 == 0 and year % 100) else f'13.09.{year}'
