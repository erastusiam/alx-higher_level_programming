#!/usr/bin/python3

"""The first line of code defines a class Square."""


class Square:
    """This represent a square."""

    def __init__(self, size=0):
        """Initialize a new square with a given size.
        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """This gets the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size of the square.
        Args:
            value (int): The new size of the square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size ** 2)
