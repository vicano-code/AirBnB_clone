#!/usr/bin/python3
"""
Module - BaseModel

-Defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Defines all common attributes/methods for other classes

    Attributes:
        - id: string
        - created_at: datetime
        - updated_at: datetime
    Methods:
        - __init__(self, id=None, created_at=None, updated_at=None)
        - __str__(self)
        - save(self)
        - to_dict(self)

    """

    def __init__(self, *args, **kwargs):
        """initialize atributes"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        '''parse the string back into a datetime'''
                        setattr(self, key, datetime.fromisoformat(value))
                    else:
                        setattr(self, key, value)


    def __str__(self):
        """override the in-built str method"""
        return "[{:s}] ({:s}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """updates the  attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

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
