#!/usr/bin/python3
"""
This module contains the following function:
    text_indentation - Prints text with 2 newlines after
                        ., ? and :
"""


def text_indentation(text):
    """
    Prints text with 2 newlines after '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for c in text:
        if c == '.' or c == '?' or c == ':':
            print(c + "\n\n", end='')
        else:
            print(c, end='')
