
import re

# Solving this problem requires 2 regex: One to check 6 digit inclusive 1000000 to 999999 and another to check
# for alternating digits, in the form of x?x, like 101
#
# The first one was simple. The first digit can be from 1-9 while the other 5 is 0-9
# The second one was more complicated but still not the hardest. Since it does count overlapping, like
#  1010, there are 2 such alternating digits - 101 and 010. So we'll need to use lookaheads and capturing
# group for this
#
# (\d) - Capture a digit
# (?=...) - Lookahead
# .     - Any middle digit
# \1    - First captured digit
#
# Since it cannot have more than 1 such alternating digits, run a regex searchall check, and see if all
# such match is count less than 2.

def soln1():
    regex_integer_in_range = re.compile( r'^[1-9][0-9]{5}$' )
    regex_alternative_repetitive_digit_pair = re.compile( r'(\d)(?=.\1)' )

    postal_code = input()
    print( bool(re.match(regex_integer_in_range, postal_code) ) and
           len(re.findall(regex_alternative_repetitive_digit_pair, postal_code) ) < 2)
