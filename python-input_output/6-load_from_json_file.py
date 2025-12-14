#!/usr/bin/python3

''' I hate docstring '''

import json


def load_from_json_file(filename):
    ''' I hate docstring '''

    with open(filename) as f:
        return json.load(f)
