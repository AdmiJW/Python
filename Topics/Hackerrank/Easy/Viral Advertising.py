
# Quite hard to come up with O(1) equation. So since input size small, O(N) suffices

# O(N) solution
def viralAdvertising(n):
    p, res = 5, 0
    for i in range(n):
        res += p // 2
        p = (p // 2) * 3
    return res


# For recursive solution
# Each call, return people liked (n//2) with the result of recursive call on subsequent days
def viralAdvertising2(n, p=5):
    if n == 0: return 0
    return (p // 2) + viralAdvertising(n-1, (p // 2) * 3)
