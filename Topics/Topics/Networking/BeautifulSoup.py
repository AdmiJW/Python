#   Web Scraping is retrieving information from websites using program and codes (Not using browser).
#   We can retrieve information from the website by parsing the HTML contents
#   One way to do this is to use Beautiful Soup, which is a HTML parser mainly for web scraping

from urllib import parse, request, error
from bs4 import BeautifulSoup

link = 'http://py4e-data.dr-chuck.net/known_by_Saffi.html'

html = request.urlopen(link).read()

#   Constructor takes in 2 params. First is the html file, second is the type of parser
soup = BeautifulSoup(html, 'html.parser')

# Obtain the anchor tags
tags = soup('a')

# Perform operation on each individual anchor tag
for tag in tags:
    # Will print out the whole tag in HTML format
    print('TAG: ', tag)
    # Will obtain the href attribute's value
    print('URL: ', tag.get('href', None) )
    # Will print out the text node of the tag
    print('Content: ', tag.contents[0] )
    # Will return a dictionary of the attributes of the tag
    print('Attributes: ', tag.attrs)
    print()

