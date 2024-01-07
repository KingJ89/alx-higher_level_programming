#!/usr/bin/python3
    def uppercase(s):
    """Print a string in uppercase followed by a new line./n"""
    for c in s:
        if ord('a') <= ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{}".format(c), end="")
    print("")
