#!/usr/bin/python3
"""Definition of  a lookup function."""


def lookup(obj):
    """Gets all attributes and methods of an object.

    contains arguments "obj" Object to retrieve attributes and methods of,
    and returns List of attributes and methods.
    """
    return dir(obj)
