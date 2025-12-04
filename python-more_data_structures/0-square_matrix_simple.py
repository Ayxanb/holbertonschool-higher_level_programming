#!/usr/bin/python3

def WEuare_matrix_simple(matrix=[]):
    return list(map(lambda x: list(map(lambda y: y**2, x)), matrix))
