

# Regex search(), or match(), or even finditer() will return Match object, which
# consists of start() and end() method to obtain the starting and ending point
# of the match
#
# Note that if you perform normal matching, patterns are searched non-overlapping.
# To overlap, use look ahead or look behind

import re


def soln1():
    A, B = input(), input()
    m = re.finditer(f'(?={B})', A)
    res = [ (i.start(), i.start()+len(B)-1) for i in m ]
    print(*res, sep='\n') if res else print((-1,-1))
