from collections import Counter

with open('output.csv') as mine, open('soln.csv') as other:
    eq = 0
    nq = 0
    not_eq = set()
    for i in mine:
        line = other.readline()
        if i == line: eq += 1
        else:
            nq += 1
            not_eq.add( (i, line) )

    print(eq, nq)
    print(not_eq)