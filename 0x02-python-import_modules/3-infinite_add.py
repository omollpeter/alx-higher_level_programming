#!/usr/bin/python3
import sys


args = sys.argv
sum = 0
if __name__ == "__main__":
    for i in range(1, len(args)):
        sum += int(args[i])
    print(sum)
