#!/usr/bin/python3


"""
Prints numbers from 0 to 99
"""
current_num = 0

while current_num <= 99:
    if current_num != 99:
        print("{:02d}, ".format(current_num), end="")
    else:
        print(str(current_num))
    current_num += 1
