#!/usr/bin/python3
"""
This module sends a request to url, displays the body of the response
and handles exceptions
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]

    response = requests.get(url=url)
    if response.status_code >= 400:
        print("Error code:", response.status_code)
    else:
        print(response.text)
