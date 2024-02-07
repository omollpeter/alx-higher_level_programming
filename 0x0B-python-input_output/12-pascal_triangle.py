#!/usr/bin/python3
"""
This module contains the following function:
    pascal_triangle - Returns list of lists of integers representing
                        Pascal's triangle of n

"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing the Pascal's
    triangle of n
    """

    pascal = []
    list_to_add = []
    i = 1

    while i <= n:
        if i == 1:
            list_to_add.append(1)
        else:
            new = []
            for r in range(i):
                if r == 0:
                    new.append(1)
                elif r == i - 1:
                    new.append(1)
                else:
                    new.append(list_to_add[r - 1] + list_to_add[r])
            list_to_add = new
        pascal.append(list_to_add)
        i += 1
    return pascal
