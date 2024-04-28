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

    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(
                json_data.get("id"), json_data.get("name")
            ))
        else:
            print("No result")
    except Exception as e:
        print("Not a valid JSON")
