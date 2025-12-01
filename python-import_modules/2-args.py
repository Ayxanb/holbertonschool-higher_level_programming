#!/usr/bin/python3

import sys

if __name__ == '__main__':
    size = len(sys.argv) - 1
    print('{} argument{}'.format(size, 's:' if size != 1 and size != 0 else 's.' if size == 0 else ':'))

    for i, arg in enumerate(sys.argv[1:]):
        print("{}: {}".format(i+1, arg))
