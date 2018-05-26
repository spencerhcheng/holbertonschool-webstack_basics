#!/usr/bin/env python3


def weight_average(my_list=[]):
    """
    Returns weighted average of all
    integer tuples
    """
    if my_list is None or my_list == []:
        return 0

    denominator = 0
    numerator = 0

    while my_list:
        n1, n2 = my_list.pop()
        denominator += n2
        numerator += n1 * n2

    return numerator / denominator
