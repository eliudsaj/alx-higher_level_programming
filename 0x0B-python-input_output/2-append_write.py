#!/usr/bin/python3
"""Definition of the function."""


def append_file(filename="", text=""):
    """append a utf8 file at the end of the file.

    contains arguments and the filename The name and path of the file to append
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
