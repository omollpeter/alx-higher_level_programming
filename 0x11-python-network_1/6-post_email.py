#!/usr/bin/python3
"""
This module takes in a url and email and sends a post request to the
url then displays the body of the response
"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {}
    values['email'] = email

    response = requests.post(url=url, data=values)
    print(response.text)
