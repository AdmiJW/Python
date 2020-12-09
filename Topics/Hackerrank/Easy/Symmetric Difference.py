############################################################################################
# Sets
#
# > sets are created using constructor set()
# > We can add elements to set using set.add(). please note that it adds SINGLE element. Thus
#   if you add a iterable, it becomes ONE element of iterable (Not expanded)
# > To add all elements in an iterable, please use set.update()
# > We can use discard() or remove() to delete elements from a set. However difference is:
#       discard() ignores if no such element
#       remove() throws KeyError exception if no such element
# > Set operations is done by set.union(), set.intersection(), and set.difference()
#
###########################################################################################

if __name__ == '__main__':
    # Do note its better to use _ as placeholder variable
    _, setA, _, setB = int(input()), set(map(int, input().split())) \
        , int(input()), set(map(int, input().split()))

    # Difference A - B
    diffA_B = setA.difference(setB)
    # Difference B - A
    diffB_A = setB.difference(setA)

    # sorted( set ) will return a new list of sorted elements
    # Using list comprehension to print out the elements
    # Remember that we can also use + for union of two sets
    [print(x) for x in sorted( diffA_B.union(diffB_A) ) ]


def second_approach():
    # Each line will be split, become a set and stored in one large list. Then only take the second and fourth line
    setA, setB = ( set( input().split() ) for i in range(4))[1::2]
    # Using ^ (Symmetric difference, XOR) and sort it with int() function passed as key function, lastly join using '\n'
    print('\n'.join( sorted(setA ^ setB, key=int) ) )
