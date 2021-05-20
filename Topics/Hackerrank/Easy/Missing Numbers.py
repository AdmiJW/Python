from collections import Counter

# Counter solution. Keys are accessed in ascending
# O(N) space, O(N log N) time
def missingNumbers(arr, brr):
    ac = Counter(arr)
    bc = Counter(brr)
    res = []
    for i in sorted(bc.keys()):
        if bc[i] > ac[i]:
            res.append(i)
    return res


# Array Counter solution. O(N) space O(N) time
def missingNumbers(arr, brr):
    freqA = [0]*10001
    freqB = [0]*10001
    for i in arr:
        freqA[i] += 1
    for i in brr:
        freqB[i] += 1
    res = []
    for i, f in enumerate(freqB):
        if f > freqA[i]:
            res.append(i)
    return res


# Pure sorting solution. O(1) space (if not consider sorting and solution)
def missingNumbers(arr, brr):
    arr.sort()
    brr.sort()
    res = []
    i, j = 0, 0
    while j < len(brr):
        if i < len(arr) and arr[i] == brr[j]:
            i += 1
        elif not len(res) or res[-1] != brr[j]:
            res.append(brr[j])
        j += 1
    return res
