#!/usr/bin/python3

''' I hate docstring '''


def append_write(filename, text):
    ''' I hate docstring '''
    with open(filename, 'a') as f:
        return f.write(text)
