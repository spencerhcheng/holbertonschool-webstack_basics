#!/usr/bin/python3


def print_diagonal(n):
    """
    Draws a diagonal line on the terminal
    """
    if n <= 0:
        print('\n')
    else:
        count = 0
        for idx in range(n):
            print('{}'.format(count * ' '), end="")
            count += 1
            print('\\')
