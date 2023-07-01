#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""


from sys import argv
import urllib.request

if __name__ == "__main__":
    reqst = urllib.request.Request(argv[1])
    with urllib.request.urlopen(reqst) as response:
        print(response.getheader('X-Request-Id'))
