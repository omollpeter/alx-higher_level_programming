#!/usr/bin/python3
"""
This module uses GitHub API to display your id
"""


import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]
    url = f"https://api.github.com/users/{username}"

    authorization = f"Bearer {access_token}"
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": authorization,
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url=url, headers=headers)
    json_data = response.json()
    if json_data:
        print(json_data.get("id"))
    else:
        print(None)
