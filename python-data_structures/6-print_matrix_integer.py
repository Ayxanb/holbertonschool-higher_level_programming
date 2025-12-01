#!/usr/bin/python3

def print_matrix_integer(matrix):
    for list_ in matrix:
        for e in list_:
            print("{:d}".format(e), end=' ')
        print()
