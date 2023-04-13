#!/usr/bin/python3

"""This first line of code defines a class Square."""



class Square:
    """This represents a square."""


    def __init__(self, size=0):
        """This initializes a new Square.
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
        """Calculate the area of the square."""
        return self.size ** 2

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return self.size * 4

    def __str__(self):
        """Return a string representation of the square."""
        return f'Square with side length {self.size}'

    def __repr__(self):
        """Return a string representation of the square."""
        return f'Square({self.size})'

