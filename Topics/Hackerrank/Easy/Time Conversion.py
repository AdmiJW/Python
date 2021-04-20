
# To do manually, notice that minute and seconds won't change, only the hour
# changes if it is PM, not AM.


# Eg 12 hr format: 12:00:00PM
def timeConversion(s):
    converted_hr = 12 if s[:2] == '12' and s[-2:] == 'PM' else int(s[:2]) % 12 + (12 if s[-2:] == 'PM' else 0)
    return f"{converted_hr:02}:{s[3:5]}:{s[6:8]}"


# To not reinvent the wheel, use the time module
import time
def timeConversion2(s):
    t = time.strptime(s, '%I:%M:%S%p')
    return time.strftime('%H:%M:%S', t)
