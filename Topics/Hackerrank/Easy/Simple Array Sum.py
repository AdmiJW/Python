
# Seriously, in python there is a sum() function that helps you do that
# To do in functional programming way, you may use reduce() in functools module
# Or classical way, set a variable and loop thru the array, adding to variable

from functools import reduce


def soln1(arr):
    return sum(arr)

def soln2(arr):
    return reduce(lambda x,y: x+y, arr)
