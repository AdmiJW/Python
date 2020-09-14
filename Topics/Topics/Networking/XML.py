#   To parse XML files, we need to use ElementTree module

import xml.etree.ElementTree as ET
import requests

params = { 'method': 'getQuote', 'format': 'xml', 'lang': 'en' }
response = requests.get('https://api.forismatic.com/api/1.0/', params)

#   Parses the XML file. When returned, xmlFile will refer to the ROOT NODE of XML file. Therefore when using XPath,
#   use relative path
xmlFile = ET.fromstring( response.text )

print('Quote: ', xmlFile.find('./quote/quoteText').text )
print('Author: ', xmlFile.find('.//quoteAuthor').text, end='\n\n' )

response.close()


#############################################################################

response = requests.get('http://py4e-data.dr-chuck.net/comments_42.xml')

xmlFile = ET.fromstring( response.text )

#   Since there are multiple comments, it will return an array of XML elements
comments = xmlFile.findall('.//comment')
total = 0

for comment in comments:
    print('Name: ', comment.find('./name').text )
    print('Count: ', comment.find('./count').text, end='\n\n' )
    total += int( comment.find('./count').text )

print('TOTAL COUNT: ', total, end='\n\n')


#################################################################################

#   The default python xml module does not fully implement the capabilities of XML. See here for default capabilities:
#       https://docs.python.org/2/library/xml.etree.elementtree.html#supported-xpath-syntax
#
#   Therefore we need to install lxml library to use full functionality of XPath

import lxml.etree as ET2
import io

xmlFile = open('D:\\My Desktop\\Website Creating\\XML Tutorial\\XML XPath\\xpath.xml', 'rb')

#   Now xmlDOM represents the root node of the text file, which is bookstore element!
xmlDOM = ET2.parse( io.BytesIO(xmlFile.read() ) )

#   Select all the book's title
titles = xmlDOM.xpath('./book/title')

#   Unlike XPath selector which uses @ for attribute, here in Python just use element.attrib to get dictionary of
#   attributes
for title in titles:
    print('Title:', title.text, ', Language:', title.attrib['lang'] )

print()

#   Select the titles of book where the prices are below 30
below30 = xmlDOM.xpath('./book[price < 30]/title')
for title in below30:
    print('Titles Below 30: ', title.text)

print()

#   Select the titles of book where the language are english only
engOnly = xmlDOM.xpath('./book/title[@lang="en"]')
for engTitle in engOnly:
    print("Titles of English: ", engTitle.text)