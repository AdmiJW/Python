

# Brute Force solution. Time limit exceeded O(N^2)
def pairs(k, arr):
    res = 0
    for n1 in arr:
        if n1 - k == n1: continue
        for n2 in arr:
            if n1 - n2 == k:
                res += 1
                break
    return res


# In place sorting solution but with binary search. O(N log N)
def pairs(k, arr):
    arr.sort()
    res = 0
    for n1 in arr:
        if n1 - k == n1: continue
        res += binary_search(arr, n1-k)
    return res


def binary_search(arr, n):
    i,j = 0, len(arr) - 1
    while i < j:
        mid = i + (j - i) // 2
        if arr[mid] < n:
            i = mid + 1
        else:
            j = mid
    return arr[i] == n


# Two pointers approach. Since every num is unique, we can have slow and fast pointer to access each element twice
def pairs(k, arr):
    arr.sort()
    i, j, res = 0, 1, 0
    while j < len(arr):
        res += arr[j] - arr[i] == k
        if arr[j] - arr[i] > k:
            i += 1
        else:
            j += 1
    return res


# Set solution
# For each number i, check if i-k is in array, only if i-k is not equal to i itself (because array elem is unique)
def pairs(k, arr):
    nums = set(arr)
    return sum( i - k != i and i-k in nums for i in nums )


