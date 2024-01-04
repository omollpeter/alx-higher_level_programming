#!/usr/bin/python3
import sys

number = len(sys.argv) - 1
args = sys.argv
if number == 0:
    print(f"{number} argument.")
elif number == 1:
    print(f"{number} argument:")
else:
    print(f"{number} arguments:")

if number > 0:
    for index, item in enumerate(args):
        if index == 0:
            continue
        print("{0}: {1}".format(index, item))
