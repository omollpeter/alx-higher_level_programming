#!/usr/bin/python3
import sys


def print_to_err():
    info = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
    sys.stderr.write(info)
    sys.exit(1)


print_to_err()
