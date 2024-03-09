#!/usr/bin/python3
"""
Module - City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    '''
    City class inherit from BaseModel class

    Public class attributes:
        - state_id: (str) will be the State.id
        - name:     (str)
    '''
    state_id = ""
    name = ""
