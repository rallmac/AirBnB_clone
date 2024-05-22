#!/usr/bin/python3
''' This module creates a User class '''

from models.base_model import BaseModel

class State(BaseModel):
    ''' Class for managing state objects '''

    name = ""

    def __init__(self, *args, **kwargs):
        ''' Initializes the state attribute class '''
        super().__init__(*args, **kwargs)
