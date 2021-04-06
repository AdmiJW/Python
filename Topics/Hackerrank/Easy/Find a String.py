

import re

# String checking is always a kind of algorithm problem. To do it is easy, to do it efficiently is hard
#
# That aside, simply iterate thru all the possible starting indices of the main string. Then, slice the
# substring out and check if the sliced string equals the substring or not.
# Time taken is around O( (N-S)*S ) where N = length of main string, S = length of substring
#
# You may use regex for this job instead. However, regex doesn't count overlapping occurrences. Therefore
# using lookahead can resolve this issue, but problem is, each match will return empty string as result.
# In this case only number of occurrences is needed, so it's no problem


def count_substring(string, sub_string):
    length = len(sub_string)
    end = len(string) - length + 1
    return len([ i for i in range(end) if string[i:i+length] == sub_string])


def count_substring2(string, sub_string):
    pattern = re.compile(f'(?={sub_string})' )
    return len( re.findall(pattern, string) )