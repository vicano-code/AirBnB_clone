#!/usr/bin/python3
"""
Module - BaseModel

-Defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Defines all common attributes/methods for other classes

    Attributes:
        - id: string
        - created_at: datetime
        - updated_at: datetime
    Methods:
        - def __init__(self, id=None, created_at=None, updated_at=None)
        - def __str__(self)
        - def save(self)
        - def to_dict(self)

    """

    def __init__(self, id=None, created_at=None, updated_at=None):
        """initialize atributes"""
        if id is None:
            self.id = str(uuid.uuid4())
        else:
            self.id = id
        if created_at is None:
            self.created_at = datetime.now()
        else:
            self.created_at = created_at
        if updated_at is None:
            self.updated_at = datetime.now()
        else:
            self.updated_at = updated_at

    def __str__(self):
        """override the in-built str method"""
        return "[{:s}] ({:s}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
    def save(self):
        """updates the  attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
    def to_dict(self):
        """
        returns a dictionary containing all keys/values of
        __dict__ of the instance
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            dic[key] = value
        dic["created_at"] = dic["created_at"].isoformat()
        dic["updated_at"] = dic["updated_at"].isoformat()
        return dic
