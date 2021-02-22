
import re

# Breakdown of my regular expression:
#   ^                           -   Starts with
#   M{0,3}                      -   Can be 0 to 3 'M's
#   (CM|CD|D?C{0,3})            -   Either CM, CD or optional 'D' followed by at most 3 'C'
#   (XC|XL|L?X{0,3})            -   Either XC, XL or optional 'L' followed by at most 3 'X'
#   (IX|IV|V?I{0,3})            -   Either IX, IV or optional 'V' followed by at most 3 'I'

def soln1():
    pattern = re.compile("^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$")
    print( bool(re.fullmatch(pattern, input() ) ) )
