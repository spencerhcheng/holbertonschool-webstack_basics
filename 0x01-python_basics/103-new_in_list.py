#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """
    Replaces element in a list at a specific
    position without modifyiing original list
    """
    new_list = my_list[:]
    __len = len(my_list)
    if idx > __len - 1 or __len < 0:
        return new_list
    new_list[idx] = element
    return new_list
