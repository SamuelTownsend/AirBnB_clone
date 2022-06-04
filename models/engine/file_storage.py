#!/usr/bin/python3
"""
This file contains the classs: FileStorage 
"""
import json


class FileStorage:
    """
    This module takes the dict and serializes it into a JSON FILE 
    and Deserializes a JSON file 
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary of objects
        """
        return self.__objects

    def new(self, obj):
        """
        sets in the obj with the key
        """
        pass
    
    def save(self):
        """
        serializes the object to the json file
        """
        pass

    def reload(self):
        """
        deserializes the JSON file to the object
        """
        pass