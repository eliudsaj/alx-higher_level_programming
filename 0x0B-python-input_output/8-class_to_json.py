#!/usr/bin/python3
"""Definition of a Python class-to-JSON function."""


def class_to_json(obj):
    """Returns the dictionary represntation of a data structure."""
    return obj.__dict__
