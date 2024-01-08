#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not len(my_list):
        return my_list
    my_list = [False if n % 2 else True for n in my_list]
    return my_list
