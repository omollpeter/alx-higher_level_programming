#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) >= 97 and ord(c) < 123:
            c = ord(c) - 32
            c = chr(c)
        print("{}".format(c), end="")
    print("")
