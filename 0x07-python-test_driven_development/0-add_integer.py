#!/usr/bin/python3

"""
    This module adds two integers:
    add_integer
"""


def add_integer(a, b=98):
    """
    Returns the sum of a and b.
    """
    if type(a) != int and type(a) != float:
        raise TypeError('a must be an integer')
    if type(b) != int and type(b) != float:
        raise TypeError('b must be an integer')
    return int(a) + int(b)
