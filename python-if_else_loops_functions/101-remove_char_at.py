#!/usr/bin/python3
def remove_char_at(str, n):
    return ''.join(
        at[1] if at[0] != n else ''
        for at in enumerate(str)
    )
