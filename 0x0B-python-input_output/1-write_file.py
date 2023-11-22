#!/usr/bin/python3
"""Definition of the function."""


def write_file(filename="", text=""):
    """Calculates the number of lines in a file.

    contains arguments and the filename The name and path of the file to print.
    And Returns the number of lines.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
