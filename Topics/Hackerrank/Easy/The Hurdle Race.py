
# SImply obtain the maximum element of the hurdles,
# then find difference with k. If goes below negative,
# return 0

def hurdleRace(k, height):
    return min(0, max(height) - k )