
import itertools


# The Backtracking algorithm DFS solution. Using O(K) space and O( max(lengthOfArr)^K ) time complexity
def soln1():
    K, M = map(int, input().split() )
    arrs = [ tuple(map(int, input().split()[1:]) ) for i in range(K) ]

    print( recursion(arrs, 0, 0, M) )


def recursion(arrs, pos, val, M):
    if pos >= len(arrs):
        return val

    res = 0
    for i in arrs[pos]:
        next = (val * i ** 2) % M
        res = max(res, recursion(arrs, pos+1, next, M) )

    return res


# Using itertools.product to get all cartesian products of the arrays. (With the help of unpacking operator *)
# Then, reduce each cartesian product into the squared sum.
# Find out the maximum
#
# Time complexity is same since internally cartesian product is also similar algorithm as above. Space could be
# less than O( max(lengthOfArr)^K ) as Iterators don't necessary store the generated combinations. It just store
# the information to retrieve the next cartesian product.
def soln2():
    K, M = map(int, input().split())
    arrs = [tuple(map(int, input().split()[1:])) for i in range(K)]

    cartesian_products = itertools.product(*arrs)

    print(max(map(lambda x: sum(i**2 for i in x) % M, cartesian_products)))

