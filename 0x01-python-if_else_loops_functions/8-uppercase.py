#!/usr/bin/python3
def uppercase(s):
    """Converts lowercase letters to uppercase in a given string."""
    result = ""
    for c in s:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
        result += c
    return result
