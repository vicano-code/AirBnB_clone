#!/usr/bin/python3
"""
Module - Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    '''
    Amenity class inherit from BaseModel class

    Public class attribute:
        - name: (str)
    '''
    name = ""
