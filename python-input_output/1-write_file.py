#!/usr/bin/python3

''' I hate docstrings '''


def write_file(filename, text):
    ''' I hate docstrings '''
    with open(filename, 'w') as f:
        return f.write(text)
