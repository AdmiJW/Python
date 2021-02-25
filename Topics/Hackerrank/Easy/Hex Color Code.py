
import re

# This questions seems easy, but hex color codes can be easily confused with selectors!
# We need a way to differentiate hex color codes with selectors!
#
# First way is to use a boolean state to indicate whether we are inside a block of selectors
# or not!
# Search line by line. If we met with '{', it means the start of a block of CSS, and set the
# flag to true
# Conversely, once '}' is met, set boolean to False.
# Any matches of the pattern when boolean is False, is ignored




# Regex Description
# #                     Matches '#' literally
# (...)                 First matching group, so it shows full match in findall
# [a-fA-F0-9]           Valid hex color characters
# {3}                   Those hex color characters must come in combo of 3
# {1,2}                 The hex character combo of 3, can occur once or twice
#
# [{}]                  Matches character { or }
def soln1():
    pattern = re.compile(r"(#([a-fA-F0-9]{3}){1,2})")
    curly = re.compile(r"[{}]")
    isAttributes = False

    for i in range(int(input())):
        line = input()

        # Print only if there is a match AND is in CSS block
        res = re.findall(pattern, line)
        print(*[r[0] for r in res], sep='\n') if isAttributes and res else None

        # Toggle isAttributes flag
        isAttributes = not isAttributes if re.search(curly, line) else isAttributes



