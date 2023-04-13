#!/usr/bin/python3

"""This first line of the code define a class Square."""




class Square:
    """This represents a square."""


    def __init__(self, size):
        """This initializes a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.size = size


    def area(self):
        """Calculate the area of the square."""
        return self.size * self.size

    def perimeter(self):
        """Calculate the perimeter of the square."""
        return self.size * 4

    def __str__(self):
        """Return a string representation of the square."""
        return f'Square with side length {self.size}'

    def __repr__(self):
        """Return a string representation of the square."""
        return f'Square({self.size})'
