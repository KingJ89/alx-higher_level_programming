#!/usr/bin/python3
"""prints list of ascii in reverse"""
j = 0
for c in range(ord('z'), ord('a') - 1 -1):
        print("{}".format(chr(c - j)), end="")
        j = 32 if j == 0 else 0
