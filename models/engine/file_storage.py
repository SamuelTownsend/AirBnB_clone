#!/usr/bin/python3
"""heading for py file"""
import json
import models


class FileStorage:
    """ new class for storage"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """sets in the obj with the key"""
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """serializes the object to the json file"""
        json_objects = {}
        for k, v in self.__objects.items():
            json_objects[k] = value.to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to the object"""
        try:
            with open(self.__file_path, 'r') as f:
                objdict = json.load(f)
                for k in objdict.values():
                    self.__objects[k] = getattr(models, objdict[k]['__class__'](**objdict[k]))
        except Exception:
            return
