#!/usr/bin/python3
"""Defination of  a MyList subclass function."""


class MyList(list):
    """A subclass of list with a print_sorted method."""

    def print_sorted(self):
        """Prints the list sorted in ascending order."""
        print(sorted(self))
