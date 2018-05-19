#!/usr/bin/python3


def safe_print_division(a, b):
    """
    Divides 2 integers and prints result
    """
    try:
        result = a / b
        return result
    except (ZeroDivisionError, TypeError, ValueError):
        return None
    finally:
        if b == 0:
            result = None
        else:
            result = a / b
        print ("Inside result: {}".format(result))
