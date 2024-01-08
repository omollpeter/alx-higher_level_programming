#!/usr/bin/python3
def max_integer(my_list=[]):
    if not len(my_list):
        return None
    mx = my_list[0]
    for idx, num in enumerate(my_list):
        if idx == 0:
            continue
        if num > mx:
            mx = num
    return mx
