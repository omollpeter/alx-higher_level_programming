import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json


class TestBase(unittest.TestCase):
    def setUp(self):
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base(20)
        self.b4 = Base(None)
        self.b5 = Base(157)

    def tearDown(self):
        pass

    def test_instance_ids(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 20)
        self.assertEqual(self.b4.id, 3)
        self.assertEqual(self.b5.id, 157)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 100)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(sorted(json_dictionary), sorted(json.dumps(
            [{"x": 2, "width": 10, "id": 100, "height": 7, "y": 8}])))
        self.assertTrue(type(json_dictionary), str)

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, [])
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, [])

        self.assertRaises(TypeError, Base.to_json_string, [1, 2, 3])
        self.assertRaises(TypeError, Base.to_json_string, [{1, 2, 3}])
        self.assertRaises(TypeError, Base.to_json_string, [(1, 2, 3)])
        self.assertRaises(TypeError, Base.to_json_string, [None])
        self.assertRaises(TypeError, Base.to_json_string, [1.0, 1.2])

    def test_save_to_file_with_rect_instances(self):
        nb_chars = 0
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 1, 1, 32)

        Rectangle.save_to_file([rect1, rect2])
        with open("Rectangle.json", "r") as file:
            lines = file.read()
            nb_chars = len(lines)
        self.assertEqual(nb_chars, 106)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            lines = file.read()
            nb_chars = len(lines)
        self.assertEqual(nb_chars, 2)

        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            lines = file.read()
            nb_chars = len(lines)
        self.assertEqual(nb_chars, 2)
        self.assertRaises(TypeError, Rectangle.save_to_file)
        self.assertRaises(TypeError, Rectangle.save_to_file, 1)
        self.assertRaises(TypeError, Rectangle.save_to_file, [1, 2])
        self.assertRaises(TypeError, Rectangle.save_to_file, (1, 2))
        self.assertRaises(TypeError, Rectangle.save_to_file, "list_objs")

    def test_save_to_file_with_square_instances(self):
        nb_chars = 0
        sq1 = Square(10, 2, 8, 11)
        sq2 = Square(2, 1, 1, 32)

        Square.save_to_file([sq1, sq2])
        with open("Square.json", "r") as file:
            lines = file.read()
            nb_chars = len(lines)
        self.assertEqual(nb_chars, 79)

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            lines = file.read()
            nb_chars = len(lines)
        self.assertEqual(nb_chars, 2)

        Square.save_to_file([])
        with open("Square.json", "r") as file:
            lines = file.read()
            nb_chars = len(lines)
        self.assertEqual(nb_chars, 2)
        self.assertRaises(TypeError, Square.save_to_file)
        self.assertRaises(TypeError, Square.save_to_file, 1)
        self.assertRaises(TypeError, Square.save_to_file, [1, 2])
        self.assertRaises(TypeError, Square.save_to_file, (1, 2))
        self.assertRaises(TypeError, Square.save_to_file, "list_objs")
