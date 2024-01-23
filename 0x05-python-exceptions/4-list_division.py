#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                r = my_list_1[i] / my_list_2[i]
                new_list.append(r)
            except TypeError:
                new_list.append(0)
                print("wrong type")
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
    except IndexError:
        new_list.append(0)
        print("out of range")
    finally:
        len_list = list_length - len(new_list)
        if len_list:
            for n in range(len_list):
                print("out of range")
                new_list.append(0)
        return new_list
