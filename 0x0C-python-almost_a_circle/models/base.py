#!/usr/bin/python3
"""
This module contains definition for Base class

"""


import json
from pathlib import Path
import csv


class Base:
    """
    Defines Base class
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes instance attributes

        Args:
            id (int): Unique id of Base instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns JSON string representation of list_dictionaries
        """

        if isinstance(list_dictionaries, (list,)) or list_dictionaries is None:
            if type(list_dictionaries) is list:
                for _ in list_dictionaries:
                    if not isinstance(_, dict):
                        raise TypeError(
                            "list_dictionaries must be a list of dictionaries"
                        )
        else:
            raise TypeError(
                "list_dictionaries must be a list of dictionaries"
            )
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes JSON string representation of list_objs to a file
        """
        filename = cls.__name__ + ".json"

        if isinstance(list_objs, (list,)) or list_objs is None:
            if type(list_objs) is list:
                for _ in list_objs:
                    if not isinstance(_, Base):
                        raise TypeError(
                            "list_objs must be a list of instances that" +
                            " inherits from Base or None"
                        )
        else:
            raise TypeError(
                "list_objs must be a list of instances that" +
                " inherits from Base or None"
            )

        with open(filename, "w", encoding="utf-8") as file:
            list_dictionaries = []
            if list_objs is None or not len(list_objs):
                file.write("[]")
            else:
                for obj in list_objs:
                    dictionary = obj.to_dictionary()
                    list_dictionaries.append(dictionary)
                data_to_save = Base.to_json_string(list_dictionaries)
                file.write(data_to_save)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns the list of JSON string representation json_string
        """

        if not (isinstance(json_string, (str, bytes)) or json_string is None):
            raise TypeError("json_string must be a str or none")
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance with all the attributes already set
        """

        if cls.__name__ == "Rectangle":
            dummy = cls(10, 5)
            dummy.update(**dictionary)
            return dummy
        elif cls.__name__ == "Square":
            dummy = cls(10)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of instances from a json file
        """
        filename = cls.__name__ + ".json"
        path_to_file = Path(filename)

        if not path_to_file.exists():
            return []

        output = []
        with open(filename, "r") as file:
            instances = file.read()

            list_instances = cls.from_json_string(instances)
            for inst in list_instances:
                inst_details = cls.create(**inst)
                output.append(str(inst_details))
        return output

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Writes to a CSV file
        """
        if isinstance(list_objs, (list,)):
            for _ in list_objs:
                if not isinstance(_, Base):
                    raise TypeError(
                        "list_objs must be a list of instances that" +
                        " inherits from Base or None"
                    )
        else:
            raise TypeError(
                "list_objs must be a list of instances that" +
                " inherits from Base or None"
            )

        filename = cls.__name__ + ".csv"

        if cls.__name__ == "Rectangle":
            fields = ["id", "width", "height", "x", "y"]
            with open(filename, "w") as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()

                obj_dictionaries = []
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    obj_dictionaries.append(obj_dict)
                for obj in obj_dictionaries:
                    writer.writerow(obj)

        elif cls.__name__ == "Square":
            fields = ["id", "size", "x", "y"]
            with open(filename, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()

                obj_dictionaries = []
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    obj_dictionaries.append(obj_dict)
                for obj in obj_dictionaries:
                    writer.writerow(obj)

    @classmethod
    def load_from_file_csv(cls):
        """
        Reads from a CSV file
        """

        filename = cls.__name__ + ".csv"

        path_to_file = Path(filename)

        if not path_to_file.exists():
            return []

        list_instances = []
        with open(filename, "r") as file:
            csv_reader = csv.DictReader(file)

            for row in csv_reader:
                if len(row) == 5:
                    list_instances.append("[{}] ({}) {}/{} - {}/{}".format(
                        "Rectangle",
                        row["id"],
                        row["x"],
                        row["y"],
                        row["width"],
                        row["height"]
                    ))
                elif len(row) == 4:
                    list_instances.append("[{}] ({}) {}/{} - {}".format(
                        "Square",
                        row["id"],
                        row["x"],
                        row["y"],
                        row["size"],
                    ))
        return list_instances

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Opens a window then draws all Rectangles and Squares
        """
        pass
