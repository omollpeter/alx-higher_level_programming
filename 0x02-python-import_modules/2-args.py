#!/usr/bin/python3
import sys

number = len(sys.argv) - 1
args = sys.argv
if number == 0:
    print(f"{number} arguments.")
elif number == 1:
    print(f"{number} argument:")
else:
    print(f"{number} arguments:")

if number > 0:
    for i in range(1, number + 1):
        print("{0}: {1}".format(i, args[i]))
