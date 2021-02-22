import re

# This regular expression is simple.
#
# Check if the string starts with 7,8 or 9. Then, check if it is followed by exactly 9 digits.

def soln1():
    pattern = re.compile("^[789][0-9]{9}$")
    print( *["YES" if bool( re.match(pattern, input() ) ) else "NO" for i in range(int(input() ) )], sep='\n' )

soln1()