#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) >= n or len(str) * -1 < n:
        return (str)
    return str.replace(str[n], '')
