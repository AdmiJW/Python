import xml.etree.ElementTree as etree


# Finding out the depth of a xml tree, is equivalent to the problem of finding out the
# maximum depth of a normal tree. Since XML itself is already a tree
#
# We can do this via BFS (level-order-traversal), or DFS. In this solution, we used
# DFS.
# The recursion function, given element, will return the depth of it's child, without
# including the node itself. The inclusive of the node part will be done in parent
# function call, which suits the problem requirements


xml_str = '\n'.join( input() for i in range(int(input() ) ) )
root = etree.ElementTree( etree.fromstring(xml_str) )


def soln1(element):
    res = 0
    if len(element):
        res = max( soln1(child)+1 for child in element )
    return res


print(soln1(root) )
