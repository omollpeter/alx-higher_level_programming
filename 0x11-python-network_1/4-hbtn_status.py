#!/usr/bin/python3
"""
This module fetches resource from a specified url using requests module
"""


import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url=url)
    print(f"""Body response:\n\
\t- type: {type(response.text)}\n\
\t- content: {response.text}""")
