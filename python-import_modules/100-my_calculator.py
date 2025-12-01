#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])

    star = chr(42)  # generates "*"

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == star:
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, {}, /".format(star))
        exit(1)

    print("{} {} {} = {}".format(a, op, b, result))
