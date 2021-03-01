
from html.parser import HTMLParser

# The HTML parser module in Python, has a handy method: 'handle_starttag'
# This method helps parse start tags along with its attributes. We can simply
# Access those through the parameter of the function
#
# Attrs comes in the form of a list of tuples, which tuple takes the form
# (attribute, value)


class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print( f"-> {attrs[0]} > {attrs[1]}" )


parser = MyParser()
for i in range(int(input() ) ):
    parser.feed(input() )