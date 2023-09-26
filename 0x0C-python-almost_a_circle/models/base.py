#!/usr/bin/python3
"""Module: base"""
import json
import csv


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
        load_from_file(cls)
        save_to_file_csv(cls, list_objs)
        load_from_file_csv(cls)
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

    @classmethod
    def load_from_file(cls):
        """Returns list of instances."""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode="r", encoding="utf-8") as f:
                my_list = cls.from_json_string(f.read())
        except Exception as e:
            return []
        return [cls.create(**x) for x in my_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """CSV serialization method."""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w', newline='') as f:
            w = csv.writer(f)
            for obj in list_objs:
                if cls.__name__ == "Rectangle":
                    w.writerow([obj.id, obj.width, obj.height, obj.x, obj.y])
                if cls.__name__ == "Square":
                    w.writerow([obj.id, obj.size, obj.x, obj.y])
        return None

    @classmethod
    def load_from_file_csv(cls):
        """CSV deserialization method."""
        my_list = []
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="r", encoding="utf-8", newline="") as f:
            r = csv.reader(f)
            square = ["id", "size", "x", "y"]
            rectangle = ["id", "width", "height", "x", "y"]
            for line in r:
                objects = {}
                if cls.__name__ == "Rectangle":
                    for x, y in zip(rectangle, line):
                        objects[x] = y
                elif cls.__name__ == "Square":
                    for x, y in zip(rectangle, line):
                        objects[x] = y
                my_list.append(cls.create(**objects))
        return my_list
