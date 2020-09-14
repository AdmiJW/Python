#   There is a module called Requests which we can use to make HTTP requests easily, like javascript's fetch API

import requests
import json

#   Request methods:
#   requests.get(url, params, args)             - Sends a GET request
#   requests.post(url, data, json, args)        - Sends a POST request
#   requests.request(method, url, args)         - Sends a request with specified method
#   requests.delete(url, args)                  - Sends a DELETE request
#   requests.head(url, args)                    - Sends a HEAD request
#   requests.patch(url, data, args)             - Sends a PATCH request
#   requests.put(url, data, args)               - Sends a PUT request

#   After using one of above, it will return a requests.Response object
#   res.close()             - Close connection to server
#   res.content             - Return the content of response in bytes
#   res.cookies             - Return CookieJar object with cookies sent back
#   res.elapsed             - Return a timedelta object, showing time elapsed from sending to arrival
#   res.encoding            - Returns the encoding used to decode res.text
#   res.headers             - Returns a dictionary of response headers
#   res.json()              - Returns a JSON object of result
#   res.text                - Returns content of response in unicode
#   res.ok                  - Returns boolean. True if status_code less than 200
#   res.iter_content()      - Returns an iterator, which can be used in for loop. By default one item for each
#                             character
#   res.iter_lines()        - Returns an iterator, which can be used in for loop


#   Using the get request, we can pass in a dictionary of key value pairs of Query Parameters
params = {'_limit': 10}
fhand = requests.get('https://jsonplaceholder.typicode.com/todos', params)

jsonfile = fhand.json()

for obj in jsonfile:
    title = obj['title']
    done = 'YES' if obj['completed'] else 'NO'
    print('Title: {}\nCompleted: {}\n'.format(title, done) )


fhand.close()