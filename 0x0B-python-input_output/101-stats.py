#!/usr/bin/python3
"""
This module contains a script that reads stdin line by line

"""


import sys


i = 0
stat_codes = []
file_size = 0
total_200 = 0
total_301 = 0
total_400 = 0
total_401 = 0
total_403 = 0
total_404 = 0
total_405 = 0
total_500 = 0

try:
    lines = sys.stdin

    for line in lines:
        line = line.split("\"")
        stat_size = line[2].split()

        stat_code = int(stat_size[0])
        size = int(stat_size[1])

        stat_codes.append(stat_code)
        file_size += size

        i += 1
        if i % 10 == 0:
            for n in stat_codes:
                if n == 200:
                    total_200 += 1
                elif n == 301:
                    total_301 += 1
                elif n == 400:
                    total_400 += 1
                elif n == 401:
                    total_401 += 1
                elif n == 403:
                    total_403 += 1
                elif n == 404:
                    total_404 += 1
                elif n == 405:
                    total_405 += 1
                elif n == 500:
                    total_500 += 1
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
