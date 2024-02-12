import unittest
from models.base import Base
from models.rectangle import Rectangle
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
