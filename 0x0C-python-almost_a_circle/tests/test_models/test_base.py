import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import json
import csv


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

    def test_to_json_string_rect_instaces(self):
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

    def test_to_json_string_square_instances(self):
        s1 = Square(10, 2, 8, 100)
        dictionary = s1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(sorted(json_dictionary), sorted(json.dumps(
            [{"x": 2, "size": 10, "id": 100, "y": 8}])))
        self.assertTrue(type(json_dictionary), str)

        json_dictionary = Base.to_json_string([])
        self.assertEqual(json_dictionary, [])
        json_dictionary = Base.to_json_string(None)
        self.assertEqual(json_dictionary, [])

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

        Rectangle.save_to_file(None)
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

        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            lines = file.read()
            nb_chars = len(lines)
        self.assertEqual(nb_chars, 2)
        self.assertRaises(TypeError, Square.save_to_file)
        self.assertRaises(TypeError, Square.save_to_file, 1)
        self.assertRaises(TypeError, Square.save_to_file, [1, 2])
        self.assertRaises(TypeError, Square.save_to_file, (1, 2))
        self.assertRaises(TypeError, Square.save_to_file, "list_objs")

    def test_static_from_json_string(self):
        r1 = Rectangle(10, 7, 2, 8, 100)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        from_json = Base.from_json_string(json_dictionary)
        self.assertEqual(
            from_json,
            [{"x": 2, "width": 10, "id": 100, "height": 7, "y": 8}]
        )
        self.assertTrue(type(from_json), list)

        json_dictionary = Base.to_json_string([])
        from_json = Base.from_json_string("")
        self.assertEqual(from_json, [])
        from_json = Base.from_json_string(None)
        self.assertEqual(from_json, [])

        self.assertRaises(json.decoder.JSONDecodeError,
                          Base.from_json_string, "list")
        self.assertRaises(json.decoder.JSONDecodeError,
                          Base.from_json_string, b"list")
        self.assertRaises(TypeError, Base.from_json_string, (1, 2, 3))
        self.assertRaises(TypeError, Base.from_json_string, "[{'a': 4}]", 5)

    def test_method_create_with_rect(self):
        dictionary = {'id': 1, 'width': 3, 'height': 5, 'x': 1, 'y': 5}
        rect1 = Rectangle.create(**dictionary)
        self.assertEqual(rect1.id, 1)
        self.assertEqual(rect1.width, 3)
        self.assertEqual(rect1.height, 5)
        self.assertEqual(rect1.x, 1)
        self.assertEqual(rect1.y, 5)
        self.assertEqual(str(rect1), "[Rectangle] (1) 1/5 - 3/5")

    def test_method_create_with_square(self):
        dictionary = {'id': 21, 'size': 3, 'x': 7, 'y': 4}
        sq1 = Square.create(**dictionary)
        self.assertEqual(sq1.id, 21)
        self.assertEqual(sq1.size, 3)
        self.assertEqual(sq1.x, 7)
        self.assertEqual(sq1.y, 4)

    def test_load_from_file_rect(self):
        r1 = Rectangle(10, 7, 2, 8, 112)
        r2 = Rectangle(2, 4, id=54)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output, [
            "[Rectangle] (112) 2/8 - 10/7",
            "[Rectangle] (54) 0/0 - 2/4"
        ])

    def test_load_from_file_square(self):
        s1 = Square(5, id=5)
        s2 = Square(7, 9, 1, 6)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertEqual(list_squares_output, [
            "[Square] (5) 0/0 - 5",
            "[Square] (6) 9/1 - 7"
        ])

    def test_load_from_file_csv_rect(self):
        r1 = Rectangle(10, 7, 2, 8, 112)
        r2 = Rectangle(2, 4, id=54)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output, [
            "[Rectangle] (112) 2/8 - 10/7",
            "[Rectangle] (54) 0/0 - 2/4"
        ])

    def test_load_from_file_csv_square(self):
        s1 = Square(5, id=5)
        s2 = Square(7, 9, 1, 6)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertEqual(list_squares_output, [
            "[Square] (5) 0/0 - 5",
            "[Square] (6) 9/1 - 7"
        ])

    def test_save_to_file_csv_with_rect_instances(self):
        nb_chars = 0
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 1, 1, 32)

        Rectangle.save_to_file_csv([rect1, rect2])
        with open("Rectangle.csv", "r") as file:
            reader = csv.DictReader(file)
            nb_lines = 0
            for row in reader:
                nb_lines += 1
        self.assertEqual(nb_lines, 2)

        Rectangle.save_to_file_csv([])
        with open("Rectangle.csv", "r") as file:
            reader = csv.DictReader(file)
            nb_lines = 0
            for row in reader:
                nb_lines += 1
        self.assertEqual(nb_chars, 0)

        self.assertRaises(TypeError, Rectangle.save_to_file_csv)
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, 1)
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, None)
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, [1, 2])
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, (1, 2))
        self.assertRaises(TypeError, Rectangle.save_to_file_csv, "list_objs")

    def test_save_to_file_csv_with_square_instances(self):
        nb_chars = 0
        sq1 = Square(10, 2, 8, 11)
        sq2 = Square(2, 1, 1, 32)

        Square.save_to_file_csv([sq1, sq2])
        with open("Square.csv", "r") as file:
            reader = csv.DictReader(file)
            nb_lines = 0
            for row in reader:
                nb_lines += 1
        self.assertEqual(nb_lines, 2)

        Square.save_to_file_csv([])
        with open("Square.csv", "r") as file:
            reader = csv.DictReader(file)
            nb_lines = 0
            for row in reader:
                nb_lines += 1
        self.assertEqual(nb_lines, 0)

        self.assertRaises(TypeError, Square.save_to_file_csv)
        self.assertRaises(TypeError, Square.save_to_file_csv, 1)
        self.assertRaises(TypeError, Square.save_to_file_csv, None)
        self.assertRaises(TypeError, Square.save_to_file_csv, [1, 2])
        self.assertRaises(TypeError, Square.save_to_file_csv, (1, 2))
        self.assertRaises(TypeError, Square.save_to_file_csv, "list_objs")
