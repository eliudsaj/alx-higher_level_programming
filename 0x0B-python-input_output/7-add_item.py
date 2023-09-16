#!/usr/bin/python3
"""Defination of  a base geometry class BaseGeometry."""


class BaseGeometry:
    """Reprsentation of base geometry."""

    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validating a parameter as an integer.

        Args:contains,
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Returns:
            TypeError: If the value is not an integer.
            ValueError: If the value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
