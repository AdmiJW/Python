from collections import Counter


# Counter is a useful class for Hash Map based frequency table
# Typically the Counter Hash Map is filled via its constructor
#
# We can access the Counter just like normal dictionaries, apart from through its functions
#       counter[ elem ]
#       counter.get( elem )
#
# It comes with an update() and subtract() function, which just adds or subtract 1 from value of the key
#       counter.update( key )
#       counter.subtract( key )


# Traditional Hash Map based solution. Using normal for loops
def soln1():
    _, shoes = input(), Counter(map(int, input().split()))
    earn = 0
    for customer in range(int(input())):
        size, price = map(int, input().split())
        if shoes[size]:
            earn += price
            shoes.subtract((size,))
    print(earn)


# List Compresion application to minimize lines of code
# Take advantage of that None is falsy value in Python.
def soln2():
    _, shoes = input(), Counter(map(int, input().split()))
    requests = [tuple(map(int, input().split())) for i in range(int(input()))]
    print(sum([req[1] if shoes[req[0]] and not shoes.subtract(req[0]) else 0 for req in requests]))
    # Once shoes[req[0]] is not 0, perform trick to subtract by using 'not'
