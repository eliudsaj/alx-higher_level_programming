#!/usr/bin/python3
"""
A Rectangle  module.

A module that provides a Rectangle class.
"""


class Rectangle:
    """A Rectangle class with attributes width and height,
    methods area, perimeter, print, str, repr, and del, and
    class attribute that keeps track number of instances,
    and class attribute print_symbol which is used as symbol for printing.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
        Raises:
            TypeError: If width or height is not an integer
            ValueError: If width or height is not an integer
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Gets the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Gets the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Computes the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Computes the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """Returns a rectangle with the print_symbol attribute."""
        if self.__width == 0 or self.__height == 0:
            return ""
        if self.print_symbol:
            symbol = "{}".format(self.print_symbol)
        else:
            symbol = "{}".format(Rectangle.print_symbol)
        return "\n".join([symbol * self.__width] * self.__height)

    def __repr__(self):
        """Returns a string representation of an instance."""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """Prints a message before the instance is destroyed."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Computes the larger Rectangle based on area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1
