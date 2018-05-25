#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element
    by another in a new list
    """
    new_list = my_list[:]

    for idx in range(len(new_list)):
        if new_list[idx] == search:
            new_list[idx] = replace
    return new_list
