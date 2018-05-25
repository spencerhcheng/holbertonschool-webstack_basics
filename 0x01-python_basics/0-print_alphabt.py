#!/usr/bin/python3


"""
Prints alphabets (except for q and e)
in lowercase, not followed by a new line
"""
start = 97

while (start <= 122):
    if start == 101 or start == 113:
        start += 1
        continue
    print('{}'.format(chr(start)), end="")
    start += 1
