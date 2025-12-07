#!/usr/bin/python3

def weight_average(my_list):
    if not my_list.__len__():
        return 0

    return \
        sum(map(lambda t: t[0] * t[1], my_list)) /\
        sum(map(lambda t: t[1], my_list))


my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))
