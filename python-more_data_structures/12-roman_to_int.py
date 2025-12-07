#!/usr/bin/python3

d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500
}

def roman_to_int(roman_string):
    if type(roman_string) is not str: return None
    return sum(map(lambda x: d[x], roman_string))
