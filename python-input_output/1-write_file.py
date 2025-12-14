#!/usr/bin/python3

''' I hate docstrings '''


def write_file(filename, text):
    with open(filename, 'w') as f:
        f.write(text)
