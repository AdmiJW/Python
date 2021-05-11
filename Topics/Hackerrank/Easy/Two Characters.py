

# Since input size is small (1000), brute force approach is applicable.
# Select 2 characters from the string, and try to reduce to see whether it can become
# valid alternating characters
#
# Time complexity is O(N) because input is only lowercase english characters, thus in worst case is
#   O( C(26, 2)*N) where C(26,2) is 26 choose 2 (only if you pick that algorithm)
# Even if you do not use combination, time complexity is O(26*26*N)
import itertools


def alternate(s):
    chars, res = set(s), 0
    combs = itertools.combinations(chars, 2)
    for c in combs:
        res = max(res, isValid(s, c[0], c[1]) )
    return 0 if res < 2 else res


def isValid(s, a, b):
    prev, res = '', 0
    for c in s:
        if c == a or c == b:
            if prev == '' or prev != c:
                prev = c
                res += 1
            else:
                return 0
    return res