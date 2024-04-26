#!/usr/bin/python3
"""
This module takes in a url and email and sends a post request to the
url then displays the body of the response
"""


import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {}
    values['email'] = email

    data = urllib.parse.urlencode(values)
    data = data.encode("utf-8")

    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        page = response.read().decode("utf-8")
        print(page)
