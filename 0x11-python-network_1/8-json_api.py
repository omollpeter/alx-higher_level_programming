#!/usr/bin/python3
"""
This module sends a post request to url, displays id and name from
the response body
"""


import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    data = {}
    data['q'] = q

    response = requests.post(url=url, data=data)

    json_data = response.json()
    if not json_data:
        print("No result")
        sys.exit(0)

    if type(json_data) is dict:
        print("[{}] {}".format(
            json_data.get("id"), json_data.get("name")
        ))
    else:
        print("Not a valid JSON")
