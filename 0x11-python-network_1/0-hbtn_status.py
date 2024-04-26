#!/usr/bin/python3
"""
This module fetches resources from a specified url
"""


import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        page = response.read()
        print(f"""Body response:\n\
\t- type: {type(page)}\n\
\t- content: {page}\n\
\t- utf8 content: {page.decode("utf-8")}\
""")
