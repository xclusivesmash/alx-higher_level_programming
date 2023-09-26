#!/usr/bin/python3
"""Module: base"""
import json


class Base:
    """Base Class Definition
    Args:
        id (int): input integer.
    Methods:
        __init__(self, id=None)
        to_json_string(list_dictionaries)
        save_to_file(cls, list_objs)
        from_json_string(json_string)
        create(cls, **dictionary)
    """
    # constants
    __nb_objects = 0

    # initialization
    def __init__(self, id: int = None):
        """Initialization method.
        Attributes:
            id (int): identification for each instance."""
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Serialization method: json"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = list()
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save json object to file."""
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as f:
            if list_objs is None:
                f.write([])
            else:
                json_objs = [x.to_dictionary() for x in list_objs]
                json_objs = cls.to_json_string(json_objs)
                f.write(json_objs)
        return None

    @staticmethod
    def from_json_string(json_string):
        """Deserialization process."""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Update instance attributes."""
        if cls.__name__ == "Rectangle":
            dummy = cls(2, 5)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(args=None, kwargs=dictionary)
        return dummy
