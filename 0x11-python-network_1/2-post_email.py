#!/usr/bin/python3
"""
takes in a URL and an email, sends POST request to URL with email as parameter
displays the body of the response (decoded in utf-8)
"""


from sys import argv
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = argv[1]
    parameter = {'email': argv[2]}

    data = urllib.parse.urlencode(parameter)
    data = data.encode('ascii')
    reqst = urllib.request.Request(url, data)
    with urllib.request.urlopen(reqst) as response:
        print(response.read().decode('utf-8'))
