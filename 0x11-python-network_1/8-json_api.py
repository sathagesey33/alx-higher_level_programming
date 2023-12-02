#!/usr/bin/python3
"""
Module: 5-search_user
Sends a POST request to http://0.0.0.0:5000/search_user
with a letter as a parameter and processes the response.
Displays the id and name if the response
body is properly JSON formatted and not empty.
Otherwise, displays appropriate error messages.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ''

    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}

    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
