#!/usr/bin/python3
from models.base_model import BaseModel


class Place(BaseModel):
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

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
