#!/usr/bin/python3

"""
The module is say_my_name
It prints first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Print My name is <first name> <last name>.

    Args:
        first_name (str): The first value.
        last_name (str): The second value.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))

