
from html.parser import HTMLParser

# In html.parser, there is a HTMLParser class that we can override, so when the
# parser meets any tags, comments etc, it will run the function according to our
# definition!


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start :', tag)
        for a in attrs:
            print(f'-> {a[0]} > {a[1]}')

    def handle_endtag(self, tag):
        print('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print('Empty :', tag)
        for a in attrs:
            print(f'-> {a[0]} > {a[1]}')


parser = MyHTMLParser()
for i in range( int(input() ) ):
    parser.feed( input() )