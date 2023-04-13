#!/usr/bin/python3

"""The first line of code defines a class Square."""




class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """Initialize a new square with a given size.
        Args:
            size (int): The size of the new square.
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.size = size


    def area(self):
        """Return the current area of the square."""
        return (self.size ** 2)

