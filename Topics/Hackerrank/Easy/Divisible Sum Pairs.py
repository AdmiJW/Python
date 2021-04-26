
# Brute force approach. O(N^2) time
def divisibleSumPairs(n, k, ar):
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            res += 1 if not (ar[i] + ar[j]) % k else 0
    return res


# To solve in O(N) time (Although using O(N) space) is you need to understand,
# that the modulus of two numbers, is summed when the original number is summed.
# Eg: k = 7
#       Say A = 5, then A % k = 5
#       Say B = 9, then B % k = 2
#       When A + B, their modulus is 5+2=7, Which is actually when mod 7, is 0.
#       Therefore I know A+B is divisible by k
#
#       If A=0 and B=7, they both have modulus of 0. So, they added will also result
#       in divisible by k
def divisibleSumPairs(n, k, ar):
    # Create a bucket of counters
    count = [0] * n
    res = 0
    for i in ar:
        count[i % k] += 1
    for i in range(n):
        another = (k - i) % k
        if another > i: continue
        res += (count[another] * (count[another] - 1)) // 2 if another == i else count[i] * count[another]
    return res
