#   To parse JSON is pretty easy in Python. It just almost directly translates to Arrays and Dictionaries

from typing import Dict

import json
from urllib import parse, request, error
from urllib.request import Request

requestObj = Request('https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en',
                     headers={'User-Agent': 'Mozilla/5.0'} )

resFile = request.urlopen(requestObj).read()
resStr = resFile.decode().replace("\\\'", "'")

#   If it was binary file, use json.load(). If it was string already, use loads (load string)
jsonQuote = json.loads(resStr)

#   Access JSON using python dictionary syntax
print('Quote: ', jsonQuote['quoteText'])
print('Author: ', jsonQuote['quoteAuthor'] if len(jsonQuote['quoteAuthor']) > 0 else 'No Information', end='\n\n')

########################################################################################################
#   Google MAP API
##################################################################################################

params = {'key': 42, 'address': ''}
baselink = 'http://py4e-data.dr-chuck.net/json?'


def printLocation(obj: Dict) -> None:
    if len(obj['results'] ) == 0:
        print('No Results...\n')
        return

    result = obj['results'][0]
    print('Name: ', result['address_components'][0]['long_name'])
    print('Latitude: ', result['geometry']['location']['lat'])
    print('Longitude: ', result['geometry']['location']['lng'])
    print('PlaceID: ', result['place_id'], end='\n\n')


while True:
    params['address'] = input("Enter address to search at Google Map (Leave blank to break): ")
    if len(params['address']) < 1:
        break

    #   Use urllib.parse.urlencode() to encode the query parameters to not contain any character other than ASCII
    requestObj = Request(baselink + parse.urlencode(params) )
    requestFile = request.urlopen(requestObj)

    mapResult = json.load(requestFile)
    printLocation(mapResult)
