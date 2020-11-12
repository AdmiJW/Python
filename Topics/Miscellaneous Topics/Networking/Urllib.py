#   Using sockets module to make HTTP requests are tiresome. We can use Python's urllib module for
#   more concise and shorter syntax

from urllib import request, parse, error
import json

#   Just use request.urlopen. It will automatically retrieve the response file back, which can be read immediately
#   using a for loop (Remember to decode or escape characters will still be inside!)
fhand = request.urlopen('https://jsonplaceholder.typicode.com/comments?_limit=10')

#   Printing out original response text
# for line in fhand:
#     print(line.decode(), end='')

#   Or Reformatting it to JSON
jsonfile = json.load(fhand)  # Note it can take in binary file as well as text file.

for obj in jsonfile:
    name = obj['name']
    email = obj['email']
    body = obj['body']
    print('Name: {}\nEmail: {}\nBody: {}\n'.format(name, email, body) )
