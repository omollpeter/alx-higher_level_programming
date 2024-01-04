#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


av = sys.argv
number = len(sys.argv) - 1

if __name__ == "__main__":
    if number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(av[1])
    b = int(av[3])

    if av[2] == '+':
        print("{0} + {1} = {2}".format(a, b, add(a, b)))
    elif av[2] == '-':
        print("{0} - {1} = {2}".format(a, b, sub(a, b)))
    elif av[2] == '*':
        print("{0} * {1} = {2}".format(a, b, mul(a, b)))
    elif av[2] == '/':
        print("{0} / {1} = {2}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
