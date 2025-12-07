#!/usr/bin/python3

d = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def roman_to_int(roman_string):
    if (type(roman_string) is not str) or (roman_string is None):
        return 0
    total = 0
    length = len(roman_string)
    for i in range(length):
        current_value = d[roman_string[i]]
        total += -current_value\
            if (i < length - 1) and (current_value < d[roman_string[i + 1]])\
            else current_value
    return total
