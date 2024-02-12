#!/usr/bin/python3

"""write string from txt file"""
def write_file(filename="", text=""):

    with open(filename, 'w') as file:
        return file.write(text)
