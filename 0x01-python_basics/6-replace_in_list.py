#!/usr/bin/python3


def replace_in_list(my_list, idx, element):
    """
    Replaces element of a list
    at a specific position idx
    """
    lst_len = len(my_list)
    if idx >= lst_len or idx < 0:
        return my_list
    else:
        my_list[idx] = element
    return my_list
