#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    for k in a_dictionary.keys():
        if k == key:
            del a_dictionary[key]
            return a_dictionary
    return a_dictionary
