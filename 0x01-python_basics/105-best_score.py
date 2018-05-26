#!/usr/bin/python3


def best_score(my_dict):
    """
    Returns a key with the biggest integer value
    """
    if my_dict is None:
        return None

    value_list = []
    for v in my_dict.values():
        value_list.append(v)

    best_score = max(value_list)

    for k, v in my_dict.items():
        if v == best_score:
            return k
