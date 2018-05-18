#!/usr/bin/python3


def common_elements(set_1, set_2):
    """
    Returns a set of common
    elements in two sets
    """
    unique_ele = set()
    ret_lst = []

    for ele in set_1:
        unique_ele.add(ele)
    for ele2 in set_2:
        if ele2 in unique_ele:
            ret_lst.append(ele2)
    return ret_lst
