#!/usr/bin/python3
def element_at(my_list, idx):
    elems = len(my_list) - 1
    if idx < 0:
        return
    if idx > elems:
        return
    return my_list[idx]
