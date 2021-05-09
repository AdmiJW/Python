
# Simply count the number of uppercases. Return noofUppercase+1 since first word is lowercase

def camelcase(s):
    return sum( c.isupper() for c in s ) + 1
