#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for ch in my_string:
        if ch == 'c' or ch == 'C':
            continue
        new_str += ch
    return new_str
