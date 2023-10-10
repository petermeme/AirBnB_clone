#!/usr/bin/python3

"""
This is an abstraction class to be inherited by other classes of the project
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """

    def __init__(self, *args, **kwargs):
        """Initialization"""
        self.id = str(uuid.uuid4())
        now = datetime.now()
        self.created_at = now
        self.updated_at = now
        if len(kwargs) != 0:
            for i, a in kwargs.items():
                if i == "created_at" or i == "updated_at":
                    self.__dict__[i] = datetime.strptime(a, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[i] = a

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute updated_
        at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary representation of an object"""
        res = self.__dict__
        res['__class__'] = self.__class__.__name__
        res['created_at'] = self.created_at.isoformat()
        res['updated_at'] = self.updated_at.isoformat()
        return res
