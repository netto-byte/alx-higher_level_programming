#!/usr/bin/python3
"""Defines an addition function."""


def add_integer(a, b=98):
    """Returns the sum of two operands
    Args:
        a: First operand
        b: Second operand

    float arguments are typecasted to ints

    Raises:
        TypeError: If either of a or b is non-integer or non-float.
    """

    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return int(int(a) + int(b))
