#!/usr/bin/python3
"""heading for py file"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

        
class FileStorage:
    """ new class for storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """sets in the obj with the key"""
        nameof = obj.__class__.__name__
        nameof = nameof + "." + obj.id
        self.__objects.setdefault(nameof, obj)

    def save(self):
        """serializes the object to the json file"""
        odict = {}
        for x in self.__objects: 
            odict.setdefault(x, self.__objects[x].to_dict())
        jsdic = json.dumps(odict)
        with open(self.__file_path, "w") as f:
            f.write(jsdic)

    def reload(self):
        """deserializes the JSON file to the object"""
        class_list = [BaseModel, User, State, Amenity, Place, City, Review]
        try:
            odict = {}
            odic2 = {}
            with open(self.__file_path, "r") as f:
                odict = json.load(f)
            for key in odict:
                y = odict[key]["__class__"]
                for idx, item in enumerate(class_list):
                    if y in str(item):
                        a = class_list[idx](**odict[key])
                odic2.setdefault(key, a)
            self.__objects = odic2
        except:
            pass
