#!/usr/bin/python3

def weight_average(my_list):
    if not my_list.__len__():
        return 0

    return \
        sum(map(lambda t: t[0] * t[1], my_list)) /\
        sum(map(lambda t: t[1], my_list))
