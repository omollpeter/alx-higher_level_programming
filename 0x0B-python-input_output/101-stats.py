#!/usr/bin/python3
"""
This module contains a script that reads stdin line by line

"""


import sys


i = 0
stat_codes = []
file_size = 0

try:
    for line in sys.stdin:
        if not len(line):
            sys.exit(0)
        line = line.split("\"")
        stat_size = line[2].split()

        stat_code = int(stat_size[0])
        size = int(stat_size[1])

        stat_codes.append(stat_code)
        file_size += size

        i += 1
        if i % 10 == 0:
            total_200 = stat_codes.count(200)
            total_301 = stat_codes.count(301)
            total_400 = stat_codes.count(400)
            total_401 = stat_codes.count(401)
            total_403 = stat_codes.count(403)
            total_404 = stat_codes.count(404)
            total_405 = stat_codes.count(405)
            total_500 = stat_codes.count(500)

            if file_size:
                print(f"File size: {file_size}")
            if total_200:
                print(f"200: {total_200}")
            if total_301:
                print(f"301: {total_301}")
            if total_400:
                print(f"400: {total_400}")
            if total_401:
                print(f"401: {total_401}")
            if total_403:
                print(f"403: {total_403}")
            if total_404:
                print(f"404: {total_404}")
            if total_405:
                print(f"405: {total_405}")
            if total_500:
                print(f"500: {total_500}")
except KeyboardInterrupt:
    total_200 = stat_codes.count(200)
    total_301 = stat_codes.count(301)
    total_400 = stat_codes.count(400)
    total_401 = stat_codes.count(401)
    total_403 = stat_codes.count(403)
    total_404 = stat_codes.count(404)
    total_405 = stat_codes.count(405)
    total_500 = stat_codes.count(500)

    if file_size:
        print(f"File size: {file_size}")
    if total_200:
        print(f"200: {total_200}")
    if total_301:
        print(f"301: {total_301}")
    if total_400:
        print(f"400: {total_400}")
    if total_401:
        print(f"401: {total_401}")
    if total_403:
        print(f"403: {total_403}")
    if total_404:
        print(f"404: {total_404}")
    if total_405:
        print(f"405: {total_405}")
    if total_500:
        print(f"500: {total_500}")
    raise

if i % 10:
    total_200 = stat_codes.count(200)
    total_301 = stat_codes.count(301)
    total_400 = stat_codes.count(400)
    total_401 = stat_codes.count(401)
    total_403 = stat_codes.count(403)
    total_404 = stat_codes.count(404)
    total_405 = stat_codes.count(405)
    total_500 = stat_codes.count(500)

    if file_size:
        print(f"File size: {file_size}")
    if total_200:
        print(f"200: {total_200}")
    if total_301:
        print(f"301: {total_301}")
    if total_400:
        print(f"400: {total_400}")
    if total_401:
        print(f"401: {total_401}")
    if total_403:
        print(f"403: {total_403}")
    if total_404:
        print(f"404: {total_404}")
    if total_405:
        print(f"405: {total_405}")
    if total_500:
        print(f"500: {total_500}")
