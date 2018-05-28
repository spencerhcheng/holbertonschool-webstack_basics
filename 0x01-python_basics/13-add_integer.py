#!/usr/bin/python3
import sys


def add_integer(a, b):
    """
    Adds 2 integers
    """
    if isinstance(a, float) or isinstance(a, int):
        if isinstance(b, float) or isinstance(b, int):
            return int(a) + int(b)
        else:
            raise TypeError("b must be an integer")
    else:
        raise TypeError("a must be an integer")

if __name__ == "__name__":
    a = sys.argv[1]
    b = sys.argv[2]
    add_integer(a, b)
