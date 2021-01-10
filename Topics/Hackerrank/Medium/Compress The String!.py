import itertools

# The Python module itertools consists of a function groupby()
#
#       itertools.groupby( iterable, [keyfunc] )
#
# By default, it returns a key value pairs of
#       ELEMENT -> Iterator
#
# Which groups the iterable into clusters. Say we have consecutive 'A' in a string. It will return
# the iterator pointing to the first 'A', and ends when we hit the ending A
#
#       AAABBBCCCAAA
#       ^  ^  ^  ^
#       Iterators


# Traditional, readable method
def soln1():
    s = input()
    for k,v in itertools.groupby(s):
        occurrence = len( tuple(v) )
        print( '({}, {})'.format(occurrence, k), end=' ' )


# Compressed solution using generator comprehension and unpacking operator *
def soln2():
    print( *( (len( tuple(v) ), int(k) ) for k, v in itertools.groupby(input() ) ) )
