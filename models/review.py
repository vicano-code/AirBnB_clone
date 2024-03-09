#!/usr/bin/python3
"""
Module - Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    '''
    Review class inherit from BaseModel class

    Public class attributes:
        - place_id:     (str) will be the Place.id
        - user_id:      (str) will be the User.id
        - text:         (str)
    '''
    place_id = ""
    user_id = ""
    text = ""
