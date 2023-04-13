#!/usr/bin/python3

"""This defines a class Square."""



class Square:
    """This represents a square."""

    def __init__(self, size=0):
        """This initialize a new square with a given size.
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

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
        else:
            [print("#" * self.__size) for i in range(self.__size)]
