#!/usr/bin/python3

def islower(c):
    """
    Checks if a character is
    lowercase
    """
    if ord(c) > 96 and ord(c) < 123:
        return True
    else:
        return False

if __name__ == "__main__":
    islower(c)
