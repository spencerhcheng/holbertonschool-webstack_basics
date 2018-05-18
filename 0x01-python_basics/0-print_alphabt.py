#!/usr/bin/python3

def print_alphabt():
    start = 97

    while (start <= 122):
        if start == 101 or start == 113:
            start += 1
            continue
        print(chr(start), end="")
        start += 1

if __name__ == "__main__":
    print_alphabt()
