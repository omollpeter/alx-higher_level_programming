#!/usr/bin/python3
"""
This module uses GitHub API to display 10 commits for a user
"""


import sys
import requests


if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"

    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28"
    }

    response = requests.get(url=url, headers=headers)
    commits = response.json()
    if commits:
        for i in range(10):
            author = commits[i].get("commit").get("author")
            print("{}: {}".format(
                commits[i].get("sha"), author.get("name")
            ))
