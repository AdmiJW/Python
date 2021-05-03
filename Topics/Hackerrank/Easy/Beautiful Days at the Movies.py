

# Is easy to do by string parsing. Reversing a number by reversing the string itself
# then perform check.
# Time is O(N).

def beautifulDays(i, j, k):
    count = 0
    for n in range(i, j+1):
        rev = int(str(n)[::-1] )
        count += 0 if ((n + rev) % k) else 1
    return count
