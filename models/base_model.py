#!/usr/bin/python3
"""
Module contains the Superclass: BaseModel
"""
from datetime import datetime 
import uuid
import json

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
                if k == 'created_at':
                    v = datetime.fromisoformat(v)
                    setattr(self, k, v)
        else:
            self.id = uuid.uuid4()
            self.created_at = datetime.now()
            self.updated_at = self.created




    def to_json_string(self):
        """
        string for printing 
        """
        return json.dumps(self.to_dict())


    def save(self):
        """
        updates the public instance attribute with the current datetime
        """
        pass


    def to_dict(self):
        """
        Returns a dictionary containing all key/values of the instance
        """
        new_dict = {}
        #for k, v in self.__dict