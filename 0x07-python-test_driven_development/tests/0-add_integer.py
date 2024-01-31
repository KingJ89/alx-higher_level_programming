#!/usr/bin/python3

"""
The module is add_integer.
It adds two integers together.
"""


def add_integer(a, b=98):
    """
    Returns the sum of two integers.

    Args:
        a (int or float): The first operand.
        b (int or float): The second operand. Default is 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    # Convert float to integer
    a = int(a) if isinstance(a, float) else a
    b = int(b) if isinstance(b, float) else b

    return a + b

