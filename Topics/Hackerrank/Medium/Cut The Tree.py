
# This is a DFS problem. Main challenge is, I am unable to use recursion due to the input size of max 10^5
#
# First, obtain the sum of all nodes in the tree. Then, we would perform DFS on the tree, changing each value
# of the node into the SUM of the subtree rooted at the recursed node. See:
#
#       (1)
#   (2)     (3)
#  (4)(5)  (6)(7)
#
# Then after DFS and summing:
#
#       (28)
#   (11)     (16)            <- The subtree sum are (4+5+2) and (6+7+3) respectively
#  (4)(5)  (6)(7)
#
# Therefore it is DFS in post-order traversal (left->right->root)
#
# Then, perform DFS again. Since all of the nodes now represent a subtree on its own, we can easily find out
# all possible edge cuts
#
# Here I use a not-so efficient iterative postorder traversal, where when I visit a node where children are unvisited,
# I push the node into stack first, then push all childrens (except parent) into stack.


def cutTheTree(data, edges):
    # Construct the Tree
    N = len(data)
    connections = list()
    for i in range(N):
        connections.append( list() )
    for n1, n2 in edges:
        connections[n1-1].append(n2-1)
        connections[n2-1].append(n1-1)

    # DFS using Stack (Because of Recursion limit).
    subtree_sum = dict()
    stack = [ (0, -1) ]
    while len(stack):
        node, parent = stack.pop()
        total = data[node]
        for child in connections[node]:
            if child == parent:
                continue
            if child not in subtree_sum:
                stack.append( (node, parent) )
                [ stack.append( (c, node) ) for c in connections[node] if c != parent ]
                break
            total += subtree_sum[child]
        subtree_sum[node] = total

    # Iterate to find differences
    total = subtree_sum[0]
    return min( abs(total - 2 * subtree_sum[s] ) for s in range(1, N) )
