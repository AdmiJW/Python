
# A Graph exploration (DFS/BFS) problem. Also known as flood fill problem
#
# From the original cell, first iterate to detect any regions that we need to explore. In other words,
# find the cell that contains '1'
#
# Once that is found, we want to explore the region, and to do it, we'll use any of exploration algorithm.
# Call the exploration function with the grid and coordinates passed in
#
# To mark a grid as visited so we don't end up in infinite loop, we can mutate the original grid to make it
# '0', or use a copy of 2D boolean array
# Explore neighbors. If neighbors are '1' as well, record the coordinates of neighbor and search that in next iteration.


DIRS = ((-1,-1), (-1,0), (-1,1), (0,1), (0,-1), (1,-1), (1,0), (1,1))


def connectedCell(matrix):
    r, c = len(matrix), len(matrix[0])
    res = 0
    for r in range(r):
        for c in range(c):
            if matrix[r][c]:
                res = max(res, explore(matrix, r, c) )
    return res


# Push all awaiting to be explored coordinates into the to_explore list. Later pop them out
def explore(matrix, r, c):
    matrix[r][c] = 0
    to_explore = [(r,c)]
    size = 0
    while len(to_explore):
        size += 1
        r, c = to_explore.pop()
        for dr,dc in DIRS:
            if 0 <= r + dr < len(matrix) and 0 <= c + dc < len(matrix[0]) and matrix[r+dr][c+dc]:
                matrix[r+dr][c+dc] = 0
                to_explore.append((r+dr,c+dc))
    return size
