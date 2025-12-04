#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for e in my_list:
        new_list.append(e if e != search else replace)
    return new_list
