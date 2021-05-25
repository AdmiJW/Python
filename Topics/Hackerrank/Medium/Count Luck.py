
# A Pathfinding problem
#
# In my approach, I split the problem into 3 steps:
#   1. Search for starting cell, since is not provided
#   2. DFS to find the path to destination
#   3. Evaluate branches on the path
#
# However, it can be done in 2 steps, if in the recursion call:
#   >   I evaluate the number of branches ('.'s) beforehand (Excluding the last node where we come from)
#   >   Then, if recursion call returns True, I add 1 to the global result, if
#       and only if number of branches >= 2


DIRS = ( (-1,0), (1,0), (0,1), (0,-1) )
M, N = None, None


def countLuck(matrix, k):
    matrix = [ list(s) for s in matrix ]

    global M, N
    M, N = len(matrix), len(matrix[0])

    # Phase 1: Locate the position of starting point
    i, j = locate_start(matrix)
    # Phase 2: DFS and determine path
    path = []
    dfs_pathfinding(matrix, i, j, path)
    # Phase 3: Evaluate path branches
    # At particular cell, check number of surroundings for non-Xs. Subtract 2 because of source, and next path, and
    # subtract 1 only if it is origin cell
    uses = 0
    for idx, (i, j) in enumerate(path):
        paths = sum( (0 <= i+di < M) and (0 <= j+dj < N) and matrix[i+di][j+dj] != 'X' for di, dj in DIRS)\
                - (1 if idx == 0 else 2)
        uses += 1 if paths > 0 else 0
    return "Impressed" if uses == k else "Oops!"


# Locates the coordinates of 'M' in the matrix
def locate_start(matrix):
    for i, r in enumerate(matrix):
        for j, e in enumerate(r):
            if e == 'M':
                return i, j


# Finds the path to the '*'. Matrix will be mutated by 'V' to mark visited
def dfs_pathfinding(matrix, i, j, path):
    if not (0 <= i < M) or not (0 <= j < N) or matrix[i][j] == 'X' or matrix[i][j] == 'V':
        return False
    if matrix[i][j] == '*':
        return True

    path.append( (i,j) )
    matrix[i][j] = 'V'
    for di, dj in DIRS:
        if dfs_pathfinding(matrix, i+di, j+dj, path):
            return True
    path.pop()
    return False
