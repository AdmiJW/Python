import re

# This problem is regex problem. Let's see how it is represented in regex pattern:
# [+-]?     -   It can start with either + or -, or none
# [0-9]*    -   Followed by digits, any amount, including 0 length
# \.        -   A floating point must have a decimal, thus a dot.
# [0-9]+    -   Then lastly digits that followed by the dot. Must have at least one of them
#
# re.match() only matches the beginning of the string
# re.search() however searches the entire string for the pattern that matches
#
# Note: Instead of 0-9, you can use \d


def soln1():
    regex = re.compile('^[+-]?[0-9]*\.[0-9]+$')
    s = input()
    return bool( re.search( regex, s ) )


if __name__ == '__main__':
    print( *[ soln1() for i in range( int(input() ) ) ], sep='\n' )
