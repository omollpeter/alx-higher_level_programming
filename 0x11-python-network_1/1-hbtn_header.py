#!/usr/bin/python3
"""
This module takes in a url sends a request and displays a specific
header line
"""


import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    header_var = "X-Request-Id"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        req_header_id = response.info().get(header_var)
        print(req_header_id)
