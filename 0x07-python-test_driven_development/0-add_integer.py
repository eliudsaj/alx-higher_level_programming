#!/usr/bin/python3
"""Defination add_integer"""


def add_integer(a, b):
    """Calculates the sum of two integers

    Args:
        a: integer to add to b
        b: integer to add to a
    Raises:
        TypeError: If a or b is not an integer or float.
    Returns:
        The sum of a and b
    """
    h = list(map(lambda x: isinstance(x, (int, float)), [a, b]))

    if all(h):
        return int(a) + int(b)

    for x, y in list(zip(h, ['a', 'b'])):
        if not x:
            raise TypeError("{} must be an integer".format(y))
