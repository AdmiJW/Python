

# With such a big magnitude of number (10^6 digits), it's impossible to convert into int
# and sort naturally.
# Therefore you must realize one fact about strings: Lexicographical order
# When we sort strings, they are sorted by lexicographical order, which can be think of as dictionary order:
#       Compare character by character from left to right
#       >   If character differs, the one with lower character in ASCII is judged to be smaller than other string
#       >   If all character match, shorter string comes first.
# Since digits in ASCII is also ascending from 0 to 9, we could use this fact to our advantage!
#
# Therefore, we sort based on two factors:
#   1. If s1 is shorter, it MUST come before s2
#   2. Otherwise the length is same. Compare lexicographically


def bigSorting(unsorted):
    return sorted(unsorted, key=lambda e: (len(e), e) )