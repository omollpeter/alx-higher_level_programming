#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0
    score = 0
    weight = 0
    for grp in my_list:
        score += (grp[0] * grp[1])
        weight += grp[1]
    return score / weight
