#!/usr/bin/python3
"""Definition of a base geometry class BaseGeometry."""


class BaseGeometry:
    """Represention of a  base geometry."""

    def area(self):
        """If not implemented."""
        raise Exception("area() is not implemented")
