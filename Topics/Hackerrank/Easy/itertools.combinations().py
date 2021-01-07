import itertools

# Like permutations generation, combination generation also requires backtracking, albeit it's a little
# bit less memory hogging since each recursion only takes the part after the last element taken
#
# Anyway, Python comes with a handy library function in library itertools which is combinations,
#
#       combinations( iterable, r)
#
# which returns a generator to obtain the combinations of iterable each of length r



# Traditional, readable method
def soln1():
    s, r = input().split()
    for i in range(1,int(r)+1):
        for j in itertools.combinations(sorted(s), i):
            print(''.join(j) )


# Compressed Version using unpacking operator * and generator comprehension
def soln2():
    s,r = input().split()
    print( *(''.join(x) for i in range(1, int(r)+1) for x in itertools.combinations(sorted(s), i) ) )

