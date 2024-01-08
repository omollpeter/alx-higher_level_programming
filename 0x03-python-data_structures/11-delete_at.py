#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    len_l = len(my_list) - 1
    if idx < 0:
        return my_list
    if idx > len_l:
        return my_list
    for n in my_list:
        if my_list[idx] == n:
            my_list.remove(n)
    return my_list
