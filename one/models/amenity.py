#!/usr/bin/python3
''' This module creates the amenity class '''

from models.base_model import BaseModel

class Amenity(BaseModel):
    ''' This class manages the amenity objects '''

    name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes attributes for the amenity class'''
        super().__init__(*args, **kwargs)
