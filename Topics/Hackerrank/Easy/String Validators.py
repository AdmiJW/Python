
import re

# Python comes with a pack of string validators by itself already
#   s.isalnum()
#   s.isalpha()
#   s.isdigit()
#   s.islower()
#   s.isupper()
#
# To check whether the string contains any said character, check each character one by one is already enough
# Actually, some of it can be inferred with others. Eg: isAlpha - simply check isLower or isUpper
# If you don't care about iterating at worst, 5n times, use any() function


# Check 5 validators solution
def soln1():
    s = input()
    isAlnum, isAlpha, isDigit, isLower, isUpper = False, False, False, False, False
    for c in s:
        isAlnum = c.isalnum() or isAlnum            # If isAlnum is previously True, the value won't change to False
        isAlpha = c.isalpha() or isAlpha
        isDigit = c.isdigit() or isDigit
        isLower = c.islower() or isLower
        isUpper = c.isupper() or isUpper
    print(isAlnum, isAlpha, isDigit, isLower, isUpper, sep='\n')


# Check 3 validators solution
def soln2():
    s = input()
    isDigit, isLower, isUpper = False, False, False
    for c in s:
        isDigit = c.isdigit() or isDigit
        isLower = c.islower() or isLower
        isUpper = c.isupper() or isUpper
    print(isDigit or isLower or isUpper, isLower or isUpper, isDigit, isLower, isUpper, sep='\n')


# Regex solution
def soln3():
    s = input()
    isDigit = bool( re.search('[0-9]', s) )
    isLower = bool( re.search('[a-z]', s) )
    isUpper = bool( re.search('[A-Z]', s) )
    print(isDigit or isLower or isUpper, isLower or isUpper, isDigit, isLower, isUpper, sep='\n')