
# zip() method is going to take several iterables, and return a list of tuples where first element
# of each iterable is 'zipped' together in a single tuple, and so on with second, third elements..
#
#   For example we have [1,2,3,4] and [a,b,c,d,e]
#   zip those 2 iterables and we have
#
#   [ (1,a), (2,b), (3,c), (4,d) ]
#
#   The longer iterables will get truncated to match the shortest length one



# More traditional method. I wouldn't say more readable
def soln1():
    N, X = map(int, input().split() )
    marks = []
    for i in range(X):
        marks.append( map(float, input().split() ) )
    zipped = zip(*marks)

    for stud in zipped:
        total = 0
        for mark in stud:
            total += mark
        print( f'{total/X:.1f}' )


# Compressed solution
def soln2():
    N, X = map(int, input().split() )
    marks = [ map(float, input().split() ) for i in range(X) ]
    zipped = zip(*marks)
    avgs = map( lambda x: sum(x) / X, zipped )
    print(*avgs, sep='\n')
