#!/usr/bin/python3

"""Defintion of a base model class."""
import json
import csv
import turtle


class Base:
    """Base model.

    This is the "base" for all other classes in this project.

    Private Class Attributes:
        __nb_object (int): innitializes number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new Base.

        Args:
            id (int): The id of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
