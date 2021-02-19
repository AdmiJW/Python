
# Regex is a useful string matching utilities. If we want to replace certain patterns in a string
# specified by our regex, we can do that with re.sub().
#
# The function signature for the re.sub() looks as follows:
#       re.sub( pattern, function|str, stringToMatch, count, flags )
#
# The pattern is, you guessed it, the regex pattern that you want to match
# function|str, you can pass in a function with 1 parameters of Match object, and check
#       for values in that Match, and return the string to replace. Otherwise, if a string
#       is given, any full match will simply replace with given string
# stringToMatch is the target string to match

import re


# Use look ahead and look behind to check if front and back is spaces, but do not include the spaces
# in the match
# Note that the pipe character | need to be escaped because it represents 'OR' in regex as well!
def soln1():
    substituter = lambda match: "and" if match.group(0) == 'and' else "or"
    pattern = '(?<= )(&&|\|\|)(?= )'

    for i in range(int(input())):
        print(re.sub(pattern, substituter, input()))
