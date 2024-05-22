#!/usr/bin/python3

""" This module creates a user class """

from models.base_model import BaseModel

class User(BaseModel):
    """ This class manages user objects """

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(*args, **kwargs):
        ''' Initializes attributes for the user class '''
        super().__init__(*args, **kwargs)
