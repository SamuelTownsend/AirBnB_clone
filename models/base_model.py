#!/usr/bin/python3
"""
Module contains the Superclass: BaseModel
"""
from datetime import datetime 
import uuid

time = "%Y-%m-%dT%H:%M:%S.%f"


# Console is working as the shell
# Basemodel is what the object is
# file sotrage 

class BaseModel:
    """
    this class defines all common attributes/methods for other classes
    """
    def __init__(self, *arg, **kwargs):
        """
        Init to create/initialize the object
        """
        if kwargs:
            for k, v in kwargs.items():
                if k == 'created_at' or k == 'updated_at':
                    v = datetime.fromisoformat(v)
                if k == '__class__':
                    continue
                setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()




    def __str__(self):
        """
        string for printing 
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute with the current datetime
        """
        self.updated_at = datetime.now()


    def to_dict(self):
        """
        Returns a dictionary containing all key/values of the instance
        """
        new_dict = {}
        for key, value in self.__dict__.items():
            new_dict[key] = value
            new_dict['__class__'] = type(self).__name__
            new_dict['created_at'] = datetime.isoformat(self.created_at)
            new_dict['updated_at'] = datetime.isoformat(self.updated_at)
                        
        return new_dict
