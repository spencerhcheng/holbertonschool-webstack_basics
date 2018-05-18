#!/usr/bin/python3


def print_sorted_dictionary(my_dict):
    """
    Prints a dictionary ordered by keys
    """
    sorted_keys = sorted(my_dict)

    for k in sorted_keys:
        print("{}: {}".format(k, my_dict[k]))
