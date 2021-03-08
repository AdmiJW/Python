import xml.etree.ElementTree as etree


# Python does comes with a nice XML parser, in the module xml.etree.ElementTree
# here I'll use aliasing for this class, named 'etree'
#
# The ElementTree can be constructed from constructor etree.ElementTree( Element )
# which Element can be obtained from strings, using etree.fromString( str )
#
# Once parsed, we can access the root using
#       tree.getroot()
#
# The root can be used as iterators, which iterates over all its children:
#       for child in root:
#           ...
#
# Each element has a attrib property, which is a dictionary of attribute keys and values
# This is exactly what we need to solve the problem.
#
# Here I've used recursion. If you don't want, you can push unexplored child elements into
# a Stack or something as well!


def get_attr_scores(root):
    score = len( root.attrib )
    for child in root:
        score += get_attr_scores(child)
    return score


xml_str = '\n'.join( input() for i in range(int(input() ) ) )
tree = etree.ElementTree( etree.fromstring(xml_str) )

print(get_attr_scores( tree.getroot() ) )
