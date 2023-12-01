#!/usr/bin/python3
"""
Module: 0-hbtn_status
Fetches https://alx-intranet.hbtn.io/status using the requests package
Displays the body of the response in a specific format
"""

import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)
    print("Body response:")
    print("\t- type:", type(response.content))
    print("\t- content:", response.content.decode('utf-8'))
