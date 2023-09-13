#!/usr/bin/python3
"""Defines a inherits_from() function."""

def inherits_from(obj, a_class):
    """a function that returns True if the object is an instance of a class"""

     return isinstance(obj, a_class) and type(obj) != a_class
