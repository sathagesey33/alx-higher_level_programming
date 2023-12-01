#!/usr/bin/python3
"""
Module: 2-post_email
Sends a POST request to a URL with an email as
a parameter and displays the body of the response.
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    response = requests.post(url, data=payload)

    print(response.text)
