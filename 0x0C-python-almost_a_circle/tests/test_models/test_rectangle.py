import unittest
from models.rectangle import Rectangle
import sys
from io import StringIO


class TestRectangleId(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(5, 4, 2, 2, 12)

    def tearDown(self):
        pass

    def test_rect_instance_id(self):
        self.assertEqual(self.r1.id, 4)
        self.assertEqual(self.r2.id, 5)
        self.assertEqual(self.r3.id, 12)


class TestRectangleObj(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10)
        self.r3 = Rectangle(5, 4, 2, 2, 12)

    def tearDown(self):
        pass

    def test_width(self):
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 5)
        self.r1.width = 15
        self.assertEqual(self.r1.width, 15)
        self.assertRaises(TypeError, Rectangle, "5", 4)
        rect = Rectangle(3, 3)
        self.assertRaises(TypeError, setattr, rect, "width", "4")
        self.assertRaises(TypeError, setattr, rect, "width", [])
        self.assertRaises(TypeError, setattr, rect, "width", None)
        self.assertRaises(TypeError, setattr, rect, "width", {})
        self.assertRaises(TypeError, setattr, rect, "width", {1, 2})
        self.assertRaises(TypeError, setattr, rect, "width", 3.15)
        self.assertRaises(TypeError, setattr, rect, "width", (1, ))
        self.assertRaises(ValueError, setattr, rect, "width", 0)
        self.assertRaises(ValueError, setattr, rect, "width", -5)

    def test_height(self):
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 4)
        self.r1.height = 7
        self.assertEqual(self.r1.height, 7)
        self.assertRaises(TypeError, Rectangle, 5, "4")
        rect = Rectangle(5, 5)
        self.assertRaises(TypeError, setattr, rect, "height", "4")
        self.assertRaises(TypeError, setattr, rect, "height", [])
        self.assertRaises(TypeError, setattr, rect, "height", None)
        self.assertRaises(TypeError, setattr, rect, "height", {})
        self.assertRaises(TypeError, setattr, rect, "height", {1, 2})
        self.assertRaises(TypeError, setattr, rect, "height", 3.15)
        self.assertRaises(TypeError, setattr, rect, "height", (1, ))
        self.assertRaises(ValueError, setattr, rect, "height", 0)
        self.assertRaises(ValueError, setattr, rect, "height", -5)

    def test_x_coordinate(self):
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 2)
        self.r1.x = 15
        self.assertEqual(self.r1.x, 15)
        self.assertRaises(TypeError, Rectangle, 5, 4, "2", 2, 151)
        rect = Rectangle(3, 3)
        self.assertRaises(TypeError, setattr, rect, "x", "4")
        self.assertRaises(TypeError, setattr, rect, "x", [])
        self.assertRaises(TypeError, setattr, rect, "x", None)
        self.assertRaises(TypeError, setattr, rect, "x", {})
        self.assertRaises(TypeError, setattr, rect, "x", {1, 2})
        self.assertRaises(TypeError, setattr, rect, "x", 3.15)
        self.assertRaises(TypeError, setattr, rect, "x", (1, ))
        self.assertRaises(ValueError, setattr, rect, "x", -5)

    def test_y_coordinate(self):
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r3.y, 2)
        self.r1.y = 15
        self.assertEqual(self.r1.y, 15)
        self.assertRaises(TypeError, Rectangle, 5, 4, 2, "2", 152)
        rect = Rectangle(3, 3)
        self.assertRaises(TypeError, setattr, rect, "y", "4")
        self.assertRaises(TypeError, setattr, rect, "y", [])
        self.assertRaises(TypeError, setattr, rect, "y", None)
        self.assertRaises(TypeError, setattr, rect, "y", {})
        self.assertRaises(TypeError, setattr, rect, "y", {1, 2})
        self.assertRaises(TypeError, setattr, rect, "y", 3.15)
        self.assertRaises(TypeError, setattr, rect, "y", (1, ))
        self.assertRaises(ValueError, setattr, rect, "y", -5)

    def test_area(self):
        self.assertEqual(self.r1.area(), 20)
        self.assertEqual(self.r2.area(), 20)
        self.assertEqual(self.r3.area(), 20)
        self.r1.width = 15
        self.assertEqual(self.r1.area(), 30)

    def test_str_(self):
        rect1 = Rectangle(4, 6, 2, 1, 12)
        rect2 = Rectangle(10, 8, id=54)

        self.assertEqual(str(rect1), "[Rectangle] (12) 2/1 - 4/6")
        self.assertEqual(str(rect2), "[Rectangle] (54) 0/0 - 10/8")

    def test_display(self):
        rect1 = Rectangle(2, 2, 1, 1, 57)
        captured_output = StringIO()
        sys.stdout = captured_output

        rect1.display()
        printed = captured_output.getvalue()

        sys.stdout = sys.__stdout__
        self.assertEqual(printed, "\n ##\n ##\n")
