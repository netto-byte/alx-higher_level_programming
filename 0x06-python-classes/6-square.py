#!/usr/bin/python3
"""Defines a class."""


class Square:
    """A Square class."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes an instance of Squares."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get/Set a position."""
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(n, int) for n in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integrs")
        self.__position = value

    def area(self):
        """Returns the current Square area."""
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            [print() for a in range(self.__position[1])]
            for i in range(self.__size):
                [print(' ', end='') for j in range(self.__position[0])]
                [print('#', end='') for k in range(self.__size)]
                print()
