#!/usr/bin/python3
"""
This is the base model of my models. it contains the base class
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    A base class for all models with common attributes and methods.
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes a BaseModel instance with a unique ID and timestamps.
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for Key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self. key. datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())

            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

    def save(self):
        """
        Updates the `updated_at` timestamp to the current time.
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        Converts the object into a dictionary representation.
        
        Returns:
            dict: A dictionary containing object attributes.
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """
        Returns a string representation of the object.
        
        Returns:
            str: A string containing class name, ID, and attribute.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print(key, type(my_model_json[key]), "-", my_model_json[key])

