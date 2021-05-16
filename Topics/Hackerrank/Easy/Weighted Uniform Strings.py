
# This is a HashSet problem.
# To calculate all the uniform substring's weight, simply record the starting index
# of the uniform substring segment. AKA "aabbbb", the starting index of uniform
# substring segments are 0 and 2
# Once a different character is met, set the index to be current index, indicating a
# new substring segment
#
# For each character, if it is substring segment, calculate the weight with respect to
# the substring length, and store in a HashSet for quick access and answering queries later
#
# To answer queries without processing weights beforehand, we need to map the queries instead.
# Map [Weight -> indices in query array]


def weightedUniformStrings(s, queries):
    weights = set()
    last_idx = 0

    for i, c in enumerate(s):
        if c == s[last_idx]:
            weights.add( (ord(c) - ord('a') + 1) * (i - last_idx + 1) )
        else:
            last_idx = i
            weights.add( ord(c) - ord('a') + 1 )

    return ["Yes" if q in weights else "No" for q in queries]

