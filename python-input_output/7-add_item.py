#!/usr/bin/python3

''' I hate docstring '''

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

with open('add_item.json', 'w') as f:
    pass

items = load_from_json_file('add_item.json')
items.extend(sys.argv[1:])

save_to_json_file(items, 'add_item.json')
