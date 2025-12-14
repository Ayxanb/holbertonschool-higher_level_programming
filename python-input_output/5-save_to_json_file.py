#!/usr/bin/python3

''' I hate docstring '''

import json


def save_to_json_file(my_obj, filename):
    ''' I hate docstring '''

    with open(filename, 'w') as f:
        return json.dump(my_obj, f)
