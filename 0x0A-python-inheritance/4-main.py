#!/usr/bin/python3
inherits_from = __import__('4-inherits_from').inherits_from

MyList = __import__('1-my_list').MyList

a = MyList()
if inherits_from(a, list):
    print("{} inherited from class {}".format(a, list.__name__))
if inherits_from(a, MyList):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))
