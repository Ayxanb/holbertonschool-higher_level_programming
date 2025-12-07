#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return a_dictionary
    if a_dictionary.get(value) is None:
        return a_dictionary
    for key in list(a_dictionary.keys()):
        if a_dictionary[key] == value:
            del a_dictionary[key]
