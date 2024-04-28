#!/usr/bin/python3
"""
This module contains the following function:
    find_peak - Finds a peak in a list
"""


def find_peak(list_of_integers):
    """Finds a peak in a list"""
    length = len(list_of_integers)
    result = None

    if length == 0 or length == 1:
        return None
    for i in range(1, length - 1):
        if (
            list_of_integers[i] > list_of_integers[i - 1] and
            list_of_integers[i] > list_of_integers[i + 1]
        ):
            result = list_of_integers[i]
            break
    if not result:
        result = max(list_of_integers)
    return result
