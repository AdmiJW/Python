from html.parser import HTMLParser

# Since we want the end line, we either combine all lines into one single string with \n included, or
# feed into the parser one line by one line with \n concatenated at the behind.
#
# This way we can check if the comment is multilined or singlelined.


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print('>>> Multi-line Comment') if '\n' in data else print('>>> Single-line Comment')
        print(data)

    def handle_data(self, data):
        if data != '\n':
            print('>>> Data')
            print(data)


parser = MyHTMLParser()

html = '\n'.join(input() for i in range(int(input())))
parser.feed(html)


