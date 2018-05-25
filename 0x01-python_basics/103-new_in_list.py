#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replaces element in a list at a specific
    position without modifyiing original list
    """
    new_list = my_list[:]
    new_list[idx] = element
    return new_list
