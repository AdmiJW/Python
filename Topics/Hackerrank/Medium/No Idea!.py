
# More intuitive way to solve.
# Since array1 can have duplicates, we dont make it a set. Other than that, make them a set
def no_idea1():
    arr, setA, setB = [map(int, input().split()) for i in range(4)][1:]
    setA, setB = set(setA), set(setB)
    res = 0
    for i in arr:
        res += 1 if i in setA else 0
        res -= 1 if i in setB else 0
    print(res)


# Make arr a list, and the setA and setB into set in one line. Remember for destructuring *
# Generate two arrays using list comprehension, which for every occurrence in setA or B, we put 1 or -1, append them
# together and run a sum() function
def no_idea2():
    _, arr, setA, setB = input(), list(map(int, input().split() ) ), *[set(map(int, input().split() ) ) for i in range(2) ]
    print( sum( [1 for x in arr if x in setA] + [-1 for x in arr if x in setB] ) )


# Just a minor change
# Since +1 for e in setA, and -1 for e in setB, they can essentially cancel out each other, so:
def no_idea3():
    _, arr, setA, setB = input(), list(map(int, input().split())), *[set(map(int, input().split())) for i in range(2)]
    print(sum( (x in setA) - (x in setB) for x in arr) )

