#!/usr/bin/python3

"""
Module - FileStorage

A class for serialization and deserialization
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    class_dic = {"BaseModel": BaseModel}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {}
        for key, obj in self.__objects.items():
            if (type(obj) == dict):
                obj_dict[key] = obj
            else:
                obj_dict[key] = obj.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the
        JSON file (__file_path) exists ; otherwise, do nothing)
        """
        try:
            with open(self.__file_path, "r") as json_file:
                json_obj = json.load(json_file)
            for key, obj in json_obj.items():
                obj = self.class_dic[obj['__class__']](**obj)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
