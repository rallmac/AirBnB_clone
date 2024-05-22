#!/usr/bin/python3
''' Initialize the package '''
#from models.base_model import BaseModel (similar to base_models)
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
