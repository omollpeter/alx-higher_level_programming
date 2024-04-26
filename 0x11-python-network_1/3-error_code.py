#!/usr/bin/python3
"""
This module sends a request to url, displays the body of the response
and handles exceptions
"""


import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as response:
            page = response.read().decode("utf-8")
            print(page)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
