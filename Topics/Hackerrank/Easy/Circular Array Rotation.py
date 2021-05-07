
# First of all, If rotation k is more than len(a), truncate it to ensure that it is less than len(a)
# because repeated rotations
#
# Then, we don't need to do the actual rotation, just query the elements after rotation.
# Notice if query is at index i, the index of the actual element before rotation can be obtained by
# formula
#           (i + offset) % N
# and it turns out the offset is
#           len(a) - rotations
#


def circularArrayRotation(a, k, queries):
    rot = k % len(a)
    return [ a[ (q + (len(a) - rot) ) % len(a) ] for q in queries]
