#!/usr/bin/python3

''' I hate docstring '''
import json


def serialize_and_save_to_file(data, filename):
    ''' I hate docstring '''
    with open(filename, 'w') as f:
        return json.dump(data, f)

def load_and_deserialize(filename):
    ''' I hate docstring '''
    with open(filename) as f:
        return json.load(f)
