#!/usr/bin/python3

def safe_print_list(my_list, x):
    printed = 0
    try:
        for i in range(x):
            print(my_list[i], end='')
            printed += 1
    except Exception as e:
        pass
    finally:
        print()
        return printed
