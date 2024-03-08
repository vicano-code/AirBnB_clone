#!/usr/bin/python3
"""
Module - User class

-Inherits from BaseModel
"""
from models.base_model import BaseModel


class User(BaseModel):
    '''
    defines all attributes of a user

    Public class attributes:
        - email
        - password
        - first_name
        - last_name
    '''
    email = ""
    password = ""
    first_name = ""
    last_name = ""
