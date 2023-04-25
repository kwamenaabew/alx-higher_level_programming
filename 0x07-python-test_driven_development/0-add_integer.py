#!/usr/bin/python3
"""
This module is about a function that adds two numbers
"""


def add_integer(a, b=98):
    """ Addition of two numeric values and returns the results.
    This function takes two numbers a and b which can be int or
    float. The default value of b is 98.
    Args:
    a (int or float): first number to be added
    b (int or float): second number to be added

    Returns:
    int: The sum of a and b

    Raises:
    TypeError:
    If a or b are not ints or floats.
    """

    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
