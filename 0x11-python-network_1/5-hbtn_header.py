#!/usr/bin/python3
"""
This module takes in a url sends a request and displays a specific
header line
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    header_var = "X-Request-Id"

    response = requests.get(url=url)
    print(response.headers.get(header_var))
