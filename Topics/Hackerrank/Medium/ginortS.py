# This problem calls for one thing: Custom Comparators

# Initial thought: Have a function that will return a sorting key value for each character
# which will be used in sorting
#
# Lowercase - Lowest. Return its ASCII code as it is
# Uppercase - Mid. Return its ASCII plus with ASCII code of 'z' so it is always HIGHER than lowercase
# Digits - Highest. Return ASCII plus ASCII code of 'z' and 'Z'. Then, if it is even, multiply by 2 so it is
#          larger than the odd digits
def keyFinder( char: str ):
    if char.islower():
        return ord(char)
    elif char.isupper():
        return ord(char) + ord('z')
    else:
        return ( ord(char) + ord('z') + ord('Z') ) * (1 if int(char) % 2 else 2)


def soln1():
    print( ''.join(sorted( input(), key=keyFinder ) ) )


# Do you know that Python actually can compare Tuples? Python will compare element by element to determine
# if a Tuple is larger than the other, from front to back. Therefore put priority as first element of tuple
#
# 1st - Is digit and is odd
# 2nd - Is digit
# 3rd - Uppercase
# 4th - lowercase
# 5th - If all match, compare by ASCII value
def soln2():
    print( ''.join(sorted( input(), key=lambda x: (x.isdigit() and not int(x) % 2, x.isdigit(),
                                                   x.isupper(), x.islower(), x ) ) ) )


# Also, we can also categorize each character separately, sort them, then merge them finally
def soln3():
    instr = input()
    lowers, uppers, odds, evens = [x for x in instr if x.islower() ], [x for x in instr if x.isupper() ],\
                                  [x for x in instr if x.isdigit() and int(x) % 2],\
                                  [x for x in instr if x.isdigit() and not int(x) % 2 ]
    print( ''.join( (*sorted(lowers), *sorted(uppers), *sorted(odds), *sorted(evens) ) ) )
