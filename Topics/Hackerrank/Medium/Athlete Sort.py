
# This problem involves sort() function / sorted() built in, along with the key attribute
#
# Since K is given last, we can only sort everything at last in one go, using K as the index of retrieved input

def soln1():
    N, M = map(int, input().split() )
    athletes = [ tuple( map(int, input().split() ) ) for i in range(N) ]
    K = int(input() )
    athletes = map( lambda x: ' '.join( map(str, x) ), sorted( athletes, key=lambda x: x[K] ) )
    print(*athletes, sep='\n')

