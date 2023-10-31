#!/usr/bin/python3
""" a print_square function."""


def print_square(size):
    """Prints a square with a '#'.

    Args:
        size: size of the square.
    Raises:
        TypeError: If the size is not an integer
        ValueError: The size is less than 0
    """
    if not isinstance(size, (int, float)) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(int(size)):
        print("#" * int(size)
