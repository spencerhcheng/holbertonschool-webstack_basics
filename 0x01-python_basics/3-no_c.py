#!/usr/bin/python3

def no_c(str):
    """
    Removes all c and C within
    a string and returns the new
    string
    """
    new_str = ""

    for c in str:
        if c == 'c' or c == 'C':
            continue
        else:
            new_str += c
    return new_str

if __name__ == "__main__":
    no_c(str)
