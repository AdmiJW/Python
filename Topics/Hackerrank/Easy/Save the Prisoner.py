
# Some mathematics problem
# First, obtain the offset (as in the candy is distributed from chair 0, 0-indexed)
#   (m-1) % n.  Say 4 prisoners, then following pairs (candy, offset):
#       (1, 0)
#       (2, 1)
#       (3, 2)
#       (4, 3)
#       (5, 0)
#
# Then, consider the starting chair. Since chair is 1-indexed, change to 0index first, then
# after calculation, change back

def saveThePrisoner(n, m, s):
    offset = (m-1) % n
    return (s - 1 + offset) % n + 1
