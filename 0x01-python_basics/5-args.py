#!/usr/bin/python3

import sys


def args(my_args):
    """
    Prints the number of and list
    of arguments entered on the command line
    """
    num_args = len(my_args)

    if num_args == 1:
        print("{} arguments.".format(num_args - 1))
    elif num_args == 2:
        print("{} argument:".format(num_args - 1))
        print("{}: {}".format(num_args - 1, my_args[1]))
    else:
        print("{} arguments:".format(num_args - 1))
        for idx in range(1, num_args):
            print("{}: {}".format(idx, my_args[idx]))

if __name__ == "__main__":
    my_args = sys.argv
    args(my_args)
