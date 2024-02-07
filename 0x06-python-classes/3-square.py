#!/usr/bin/python3
"""Defines a class."""


class Square:
    """A Square class."""

    def __init__(self, size=0):
        """Initializes an instance of Square."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current Square area."""
        return (self.__size ** 2)
