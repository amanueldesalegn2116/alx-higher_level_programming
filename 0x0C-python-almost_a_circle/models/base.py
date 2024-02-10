#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """A base model that serves as the foundation for all other classes
    within the project 0x0C*. 

    It includes
    private class attributes:
    __nb_object (int): which stores the number of instantiated
    Base objects."""

    __nb_objects = 0

    def __init__(self, id=None):
        """The initialization process for a new instance of the Base class.

        Args:
        It specifies that the initialization requires an argument
        id (int): which represents the identity of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """A function that returns the JSON serialization of a
        list of dictionaries.

        Args:
        It takes a parameter
        list_dictionaries (list): which is a list containing dictionaries
        to be serialized into JSON format.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        """A function that writes the JSON serialization of a list of
        objects to a file.
        
        Args:
        It takes a parameter
        list_objs (list): which is a list containing instances of classes
        inherited from the Base class.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """A function that returns the deserialization of a JSON string.
        
        Args:
            json_string (str): which is a string representing a JSON list
            of dictionaries.

        Returns:
        If the json_string is None or empty, the function returns an
        empty list.
        Otherwise, it returns the Python list represented by the
        'json_string'.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """A function that returns an instance of a class instantiated
        from a dictionary of attributes.

        Args:
            **dictionary (dict): where the keys are attribute names and
            the values are attribute values to initialize the class
            instance.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """A function that returns a list of classes instantiated from
        a file containing JSON strings.

        It reads from a file named `<cls.__name__>.json`, where 
        `cls.__name__` is the name of the class.

        Returns:
            If the file does not exist, the function returns an empty list.
            Otherwise, it returns a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        """A function that writes the CSV serialization of a list of
        objects to a file.
        
        Args:
        It takes a parameter
        list_objs (list): which is a list containing instances of classes
        inherited from the Base class.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """A function that returns a list of classes instantiated from
        a CSV file.

        It reads from a file named `<cls.__name__>.csv`, where `cls.__name__`
        is the name of the class.
        
        Returns:
            If the file does not exist, the function returns an empty list.
            Otherwise, it returns a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """A function that utilizes the turtle module to draw rectangles
        and squares.

        Args:
            It takes two parameters:
            list_rectangles (list): which is a list of Rectangle objects
            to draw, and 'list_squares', which is a list of Square
            objects to draw.
        """
        turt = turtle.Turtle()
        turt.screen.bgcolor("#b7312c")
        turt.pensize(3)
        turt.shape("turtle")

        turt.color("#ffffff")
        for rect in list_rectangles:
            turt.showturtle()
            turt.up()
            turt.goto(rect.x, rect.y)
            turt.down()
            for i in range(2):
                turt.forward(rect.width)
                turt.left(90)
                turt.forward(rect.height)
                turt.left(90)
            turt.hideturtle()

        turt.color("#b5e3d8")
        for sq in list_squares:
            turt.showturtle()
            turt.up()
            turt.goto(sq.x, sq.y)
            turt.down()
            for i in range(2):
                turt.forward(sq.width)
                turt.left(90)
                turt.forward(sq.height)
                turt.left(90)
            turt.hideturtle()

        turtle.exitonclick()
