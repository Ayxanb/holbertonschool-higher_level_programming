#!/usr/bin/python3
def uppercase(str):
    for c in str:
        asci = ord(c)
        print("{}".format(c if asci>=65 and asci<=90 else chr(asci-32)), end='')

    print()

uppercase("abcdasdzzxczcvxc")
uppercase("ASDASDASDVZXCZXCZXNJEICN")
