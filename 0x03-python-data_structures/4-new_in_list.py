#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list.copy()
    elems = len(list_copy) - 1
    if idx < 0:
        return list_copy
    if idx > elems:
        return list_copy
    list_copy[idx] = element
    return list_copy
