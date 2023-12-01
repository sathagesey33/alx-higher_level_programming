#!/usr/bin/python3
"""
Module: 1-hbtn_header
Sends a request to a URL and displays the value of the X-Request-Id
variable found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        header = response.headers.get('X-Request-Id')
        print(header)
