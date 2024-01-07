#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    elems = len(my_list) - 1
    if idx < 0:
        return my_list
    if idx > elems:
        return my_list
    my_list[idx] = element
    return my_list
