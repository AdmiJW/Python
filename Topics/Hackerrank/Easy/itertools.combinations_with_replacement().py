import itertools

# Generating combinations with replacement is also very similar approach with previous ones.
# By fixing a position in each backtracking call, we can only pick the ones including the current or
# after the element selected.
#
# However, python comes with a library itertools which consists of useful functions which includes
# combinations_with_replacement().
#
#       combinations_with_replacement( iterable, r )
#
# It returns a iterator to the combinations with replacement


# Traditional, very readable solution
def soln1():
    s,r = input.split()
    combs_replacement = itertools.combinations_with_replacement( sorted(s), int(r) )

    for x in combs_replacement:
        print( ''.join(x) )


# Compressed Solution using unpacking operator *, and generator comprehension
def soln2():
    s, r = input().split()
    print( *''.join(x) for x in itertools.combinations_with_replacement(sorted(s), int(r) ) )