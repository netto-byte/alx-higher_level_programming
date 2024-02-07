#!/usr/bin/python3
"""Defines a class."""


class Square:
    """A Square class."""

    def __init__(self, size=0):
        """Initializes an instance of Squares."""
        self.size = size

    @property
    def size(self):
        """Get/Set a size"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the current Square area."""
        return (self.__size ** 2)
