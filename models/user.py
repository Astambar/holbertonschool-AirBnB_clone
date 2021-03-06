#!/usr/bin/python3
"""Module for User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Class representing a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):

        """
        The __init__ function is called automatically
        when a new instance of the class is created.
        The __init__ function can take arguments,
        but self is always the first one.
        This function serves as an initializer,
        or a constructor.

        :param self: Refer to the object itself
        :param *args: Pass a non-keyworded,
        variable-length argument list
        :param **kwargs: Pass a keyworded,
        variable-length argument list
        :return: An instance of the class
        :doc-author: Trelent
        """
        super().__init__(*args, **kwargs)
