#!/usr/bin/python3
"""Prints names in the compiled module"""

import hidden_4

if __name__ == "__main__":
    file = dir(hidden_4)
    for name in file:
        if name[:2] != "__":
            print(name)
