from collections import Counter, defaultdict


# Built in Counter and sorting solution
# Sort descending by frequency, then by ascending value of k
def migratoryBirds(arr):
    cnt = Counter(arr)
    return sorted( cnt, key=lambda k: (-cnt[k], k) )[0]


# Traditional O(N) method
# Keep a counter as well as record the maximum type and its count
# Once noticed the count equals the maximum count so far or exceeds, overwrite
def migratoryBirds2(arr):
    cnt = defaultdict(lambda: 0)
    maxtype, freq = arr[0], 0
    for i in arr:
        cnt[i] += 1
        if cnt[i] > freq:
            freq, maxtype = cnt[i], i
        elif cnt[i] == freq:
            maxtype = min(i, maxtype)
    return maxtype
