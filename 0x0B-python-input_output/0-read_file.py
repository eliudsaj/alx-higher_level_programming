#!/usr/bin/python3
"""Definition of the function."""


def read_file(filename=""):
    """Prints the contents of a text file.

    contains args and filename as the name and path of the file to print.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
