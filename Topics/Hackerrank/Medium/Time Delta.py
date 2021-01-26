from datetime import datetime

# The solution follows:
#   >   Parse string into datetime objects with specified string format
#   >   Datetime objects support arithmetic operators and will return a timedelta Object.
#   >   timeDelta object consists of total_seconds() method. Use that!

def timedelta(t1, t2):

    formatting = '%a %d %b %Y %H:%M:%S %z'

    date1, date2 = datetime.strptime(t1, formatting), datetime.strptime(t2, formatting)
    return f'{abs((date1 - date2).total_seconds()):.0f}'
