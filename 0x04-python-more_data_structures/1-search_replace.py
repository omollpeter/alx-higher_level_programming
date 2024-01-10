#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for n in my_list:
        if n == search:
            n = replace
        new_list.append(n)
    return new_list
