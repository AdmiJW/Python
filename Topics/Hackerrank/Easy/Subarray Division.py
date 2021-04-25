

# This problem calls for sliding window approach, so we can reduce the time
# complexity from O(sm) to O(s) only


# Brute force but short code solution
def birthday(s, d, m):
    return sum( 1 if sum(s[i:i+m]) == d else 0 for i in range(len(s)-m+1) )


# Sliding window solution
def birthday(s, d, m):
    res, tot = 0, sum( s[:m] )
    res += 1 if tot == d else 0
    for i in range(m, len(s) ):
        tot += s[i] - s[i-m]
        res += 1 if tot == d else 0
    return res