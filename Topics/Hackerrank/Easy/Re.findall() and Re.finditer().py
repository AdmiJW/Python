

# To deal with this problem, we need 2 concepts:
#       Regex Lookahead and Lookbehind
#       Re.findall() and Re.finditer()
#
# Re.findall() simply takes in a pattern and string, attempts to find all matching patterns and return it as string
# Re.finditer() instead of returning a list of string, it returns iterator instead
#
# Regex lookahead and lookbehind is just like normal matching of patterns, however it doesn't count towards
# overlapping rule. Say "baabaab", if i just use normal matching, it will match only the front part "aa".
# Using lookahead and lookbehind, it will match two "aa"s.
#
# Look ahead -> "(?=<thing to match>)"
# Look behind -> "(?<=<thing to match>)"

import re

vowelsPattern = '[aeiouAEIOU]'
consonantsPattern = '[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'
twoOrMore = '{2,}'

def soln1():
    pattern = re.compile( f"(?<={consonantsPattern})({vowelsPattern}{twoOrMore})(?={consonantsPattern})" )
    res = re.findall( pattern, input() )
    print( *res, sep='\n' ) if res else print(-1)
