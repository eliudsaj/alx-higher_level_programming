#!/usr/bin/python3
"""Definition of the function."""


def number_of_lines(filename=""):
    """Calculates the number of lines in a file.

    contains arguments and the filename The name and path of the file to print.
    Returns the number of lines.
    """
    count = 0
    with open(filename, encoding="utf-8") as fd:
        for line in fd:
            count += 1
    return count
