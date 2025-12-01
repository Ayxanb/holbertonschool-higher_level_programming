#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == '__main__':
    argv = sys.argv
    argv_len = len(argv)

    if argv_len != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])
    result = None

    match op:
        case '+': result = add(a, b)
        case '-': result = sub(a, b)
        case '*': result = mul(a, b)
        case '/': result = div(a, b)

        case _:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

    
    print("{} {} {} = {}".format(a, op, b, result))
