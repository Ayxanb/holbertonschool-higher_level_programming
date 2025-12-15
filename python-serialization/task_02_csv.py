#!/usr/bin/python3

''' I hate docstring '''


import csv, json


def convert_csv_to_json(filename):
    ''' I hate docstring '''

    data = []

    try:
        with open(filename, mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        with open('data.json', 'w') as json_file:
            json.dump(data, json_file)


    except AssertionError as e:
        return False

    finally:
        return True
