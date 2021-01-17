import collections
]
# An ordered Dict is simply a Dictionary where the keys are ordered based on insertion order.
#
# A normal dictionary stores the key as Sets, therefore the order of key when used in iteration
# is undefined. OrderedDict solves the problem


# Traditional, Readability Solution
def soln1():
    N = int( input() )
    items = collections.OrderedDict()

    for i in range(N):
        split = input().split()
        item, price = ' '.join( split[:-1] ), int( split[-1] )
        items[item] = items[item] + price if item in items else price

    for i in items.items():
        print(*i)

# Note: Instead of splitting, we can use rpartition() method, which does exactly just splitting the string
#       into 2 parts based on seperator provided