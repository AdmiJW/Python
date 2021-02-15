

# Regex operations usually return a Match object. Let's see how we can extract captured groups from the
# returned Match object!
#
# 1. match.group(n)
#       Returns one single capture group. Provide the index n which is the index of captured group
#       0   -   Entire match
#       1   -   First captured group
#       2   -   Second captured group.
#       and so on..
#
# 2.  match.groups()
#       Returns all the matches in one tuple of strings, excluding the full match
#
# 3.  match.groupdict()
#       If your capturing group is named, then definitely you'll use this one to return a Dictionary
#       of matches
#
# Named captured groups are used as follows:
#       '(?P<user>\w+)'             <<< named 'user'
#
#
# Also, do note that we can use backreferences in Regex. \1 refers to the first capturing group, \2 refers to the
# second and so on. Therefore
#
#       '([a-z]-\1-\1)'
#
# matches 'a-a-a' or 'z-z-z'




import re


# Re.search finds the first match and returns the Match object for it. Use backreferencing to be informed about
# what character is matched in the first capturing group!
def soln1():
    pattern = re.compile( r'([a-zA-Z0-9])\1' )
    match = re.search( pattern, input() )
    print( match.groups()[0] if match else -1 )
