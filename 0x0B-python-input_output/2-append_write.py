#!/usr/bin/python3

"""Appending File"""

def append_write(filename="", text=""):

    with open(filename, 'a') as file:
        return file.write(text)
