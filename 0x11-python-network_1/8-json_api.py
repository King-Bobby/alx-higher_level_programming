#!/usr/bin/python3
"""
takes a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


from sys import argv
import requests

if __name__ == "__main__":
    if len(argv) < 2:
        letter = ""
    else:
        letter = argv[1]
    url = "http://0.0.0.0:5000/search_user"
    parameter = {'q': letter}
    r = requests.post(url, data=parameter)
    try:
        dct = r.json()
        if dct:
            print("[{}] {}".format(dct.get('id'), dct.get('name')))
        else:
            print("No result")
    except ValueError as e:
        print("Not a valid JSON")
