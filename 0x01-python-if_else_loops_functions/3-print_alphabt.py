#!/usr/bin/python3
for alpha in range(97, 123):
    if chr(alpha) == 'q' or chr(alpha) == 'e':
        continue
    print("{0}".format(chr(alpha)), end="")
