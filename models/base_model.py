#!/usr/bin/python3
"""
    a class BaseModel that defines all common
    attributes/methods for other classes
 """

import uuid
from datetime import datetime
import models
import global_usage


class BaseModel:
    """ define the class"""
    def __init__(self, *args, **kwargs):
        """
        The __init__ function is called when an instance of a class is created.
        It can be used to set up instance variables,
        which are the variables that
        belong to each object.

        :param self: Refer to the object itself
        :param *args: Pass a non-keyworded, variable-length argument list
        :param **kwargs: Pass a dictionary of
        key/value pairs as the **arguments to the function
        :return: Nothing
        :doc-author: Trelent
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(self, key,
                                datetime.strptime(value,
                                                  '%Y-%m-%dT%H:%M:%S.%f')
                                )
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            models.storage.save()

    def __str__(self):
        """
        The __str__ function is called by the str()
        function and by the print statement to compute
        the &quot;informal&quot; string representation
        of an object. This is usually something that ends up being
        human-readable. In our case, we'll just
        return a string containing some information about this
        particular instance of our

        :param self: Refer to the instance of the class
        :return: A string that contains the class name,
        the instance id, and a printable representation of the attribute values
        :doc-author: Trelent
        """

        return "[{:s}] ({:s}) {}".format(self.__class__.__name__,
                                         self.id, self.__dict__)

    def save(self):
        """
        The save function updates the
        updated_at attribute with the current datetime

        :param self: Refer to the instance of the class
        :return: The updated_at time of the object
        :doc-author: Trelent
        """

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        The to_dict function returns a
        dictionary containing all the information
        that defines an instance of the class.
        This is useful for saving instances
        of objects in a database,
        as it provides all information needed to recreate
        the object.

        :param self: Reference
        the class instance itself
        :return: A dictionary with all
        the attributes of an object
        :doc-author: Trelent
        """
        dictionary = self.__dict__.copy()
        dictionary.update({'__class__': type(self).__name__})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary


