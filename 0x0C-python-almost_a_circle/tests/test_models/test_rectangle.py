import unittest
from models.rectangle import Rectangle
import sys
from io import StringIO


class TestRectangleId(unittest.TestCase):

    def setUp(self):
        self.r1 = Rectangle(10, 2)
        self.r2 = Rectangle(2, 10, id=5)
        self.r3 = Rectangle(5, 4, 2, 2, 12)

    def tearDown(self):
        pass

    def test_rect_instance_id(self):
        self.assertEqual(self.r1.id, 7)
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

    def test_update_id_with_args(self):
        rect1 = Rectangle(5, 5, 5, 5, 71)
        rect2 = Rectangle(10, 10)

        rect1.update(80)
        rect2.update(82)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

        rect1.update(80, 2)
        rect2.update(82, 2)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

        rect1.update(80, 2, 3)
        rect2.update(82, 2, 3)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

        rect1.update(80, 2, 3, 4)
        rect2.update(82, 2, 3, 4)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

        rect1.update(80, 2, 3, 4, 5)
        rect2.update(82, 2, 3, 4, 5)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

    def test_update_width_with_args(self):
        self.r1.update(80)
        self.r3.update(82)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r3.width, 5)

        self.r1.update(80, 2)
        self.r3.update(82, 2)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 2)

        self.r1.update(80, 2, 3)
        self.r3.update(82, 2, 3)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 2)

        self.r1.update(80, 2, 3, 4)
        self.r3.update(82, 2, 3, 4)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 2)

        self.r1.update(80, 2, 3, 4, 5)
        self.r3.update(82, 2, 3, 4, 5)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 2)

        self.assertRaises(TypeError, self.r1.update, 80, "2")
        self.assertRaises(TypeError, self.r1.update, 80, [], 3)
        self.assertRaises(TypeError, self.r1.update, 80, (1, ), 3, 4)
        self.assertRaises(TypeError, self.r1.update, 80, 3.45, 0, 4)
        self.assertRaises(TypeError, self.r1.update, 80, {1, 3}, 15, -3)
        self.assertRaises(TypeError, self.r1.update, 80, {}, 1, 2, 7)
        self.assertRaises(TypeError, self.r1.update, 80, None, None, None)
        self.assertRaises(ValueError, self.r1.update, 80, 0, 17)
        self.assertRaises(ValueError, self.r1.update, 80, -2, 5, 5)

    def test_update_height_with_args(self):
        self.r1.update(80)
        self.r3.update(82)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r3.height, 4)

        self.r1.update(80, 2)
        self.r3.update(82, 2)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r3.height, 4)

        self.r1.update(80, 2, 3)
        self.r3.update(82, 2, 3)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r3.height, 3)

        self.r1.update(80, 2, 3, 4)
        self.r3.update(82, 2, 3, 4)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r3.height, 3)

        self.r1.update(80, 2, 3, 4, 5)
        self.r3.update(82, 2, 3, 4, 5)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r3.height, 3)

        self.assertRaises(TypeError, self.r1.update, 80, 2, "2")
        self.assertRaises(TypeError, self.r1.update, 80, 2, [], 3)
        self.assertRaises(TypeError, self.r1.update, 80, 2, (1, ), 3, 4)
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3.45, 0, 4)
        self.assertRaises(TypeError, self.r1.update, 80, 2, {1, 3}, 15, -3)
        self.assertRaises(TypeError, self.r1.update, 80, 2, {}, 2, 7)
        self.assertRaises(TypeError, self.r1.update, 80, 2, None, None)
        self.assertRaises(ValueError, self.r1.update, 80, 2, 0, 17)
        self.assertRaises(ValueError, self.r1.update, 80, 2, -2, 5, 5)

    def test_update_x_with_args(self):
        self.r1.update(80)
        self.r3.update(82)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r3.x, 2)

        self.r1.update(80, 2)
        self.r3.update(82, 2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r3.x, 2)

        self.r1.update(80, 2, 3)
        self.r3.update(82, 2, 3)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r3.x, 2)

        self.r1.update(80, 2, 3, 4)
        self.r3.update(82, 2, 3, 4)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r3.x, 4)

        self.r1.update(80, 2, 3, 4, 5)
        self.r3.update(82, 2, 3, 4, 5)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r3.x, 4)

        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, "2")
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, [], 3)
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, (1, ), 3)
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, 3.45, 0)
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, {1, 3}, 15)
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, {})
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, None, None)
        self.assertRaises(ValueError, self.r1.update, 80, 2, 3, -5, 17)

    def test_update_y_with_args(self):
        self.r1.update(80)
        self.r3.update(82)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)

        self.r1.update(80, 2)
        self.r3.update(82, 2)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)

        self.r1.update(80, 2, 3)
        self.r3.update(82, 2, 3)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)

        self.r1.update(80, 2, 3, 4)
        self.r3.update(82, 2, 3, 4)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)

        self.r1.update(80, 2, 3, 4, 5)
        self.r3.update(82, 2, 3, 4, 5)
        self.assertEqual(self.r1.y, 5)
        self.assertEqual(self.r3.y, 5)

        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, 4, "2")
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, 4, [])
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, 4, (1, ))
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, 4, 3.45)
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, 4, {1, 3})
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, 4, {})
        self.assertRaises(TypeError, self.r1.update, 80, 2, 3, 4, None)
        self.assertRaises(ValueError, self.r1.update, 80, 2, 3, 17, -5)

    def test_update_id_with_kwargs(self):
        rect1 = Rectangle(5, 5, 5, 5, 71)
        rect2 = Rectangle(10, 10)

        rect1.update(id=80)
        rect2.update(id=82)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

        rect1.update(id=80, width=2)
        rect2.update(id=82, width=2)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

        rect1.update(id=80, width=2, height=3)
        rect2.update(id=82, width=2, height=3)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

        rect1.update(id=80, width=2, height=3, x=4)
        rect2.update(id=82, width=2, height=3, x=4)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

        rect1.update(id=80, width=2, height=3, x=4, y=5)
        rect2.update(id=82, width=2, height=3, x=4, y=5)
        self.assertEqual(rect1.id, 80)
        self.assertEqual(rect2.id, 82)

    def test_update_width_with_kwargs(self):
        self.r1.update(id=80)
        self.r3.update(id=82)
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r3.width, 5)

        self.r1.update(id=80, width=2)
        self.r3.update(id=82, width=2)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 2)

        self.r1.update(id=80, width=2, height=3)
        self.r3.update(id=82, width=2, height=3)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 2)

        self.r1.update(id=80, width=2, height=3, x=4)
        self.r3.update(id=82, width=2, height=3, x=4)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 2)

        self.r1.update(id=80, width=2, height=3, x=4, y=5)
        self.r3.update(id=82, width=2, height=3, x=4, y=5)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r3.width, 2)

        self.assertRaises(TypeError, self.r1.update, id=80, width="2")
        self.assertRaises(TypeError, self.r1.update, id=80, width=[], x=3)
        self.assertRaises(TypeError, self.r1.update, id=80, width=(1, ),
                          height=3, x=4)
        self.assertRaises(TypeError, self.r1.update, id=80, width=3.45, x=0,
                          y=4)
        self.assertRaises(TypeError, self.r1.update, id=80, width={1, 3},
                          height=15, x=-3)
        self.assertRaises(TypeError, self.r1.update, id=80, width={},
                          height=1, x=2, y=7)
        self.assertRaises(TypeError, self.r1.update, id=80, width=None,
                          height=None, x=None)
        self.assertRaises(ValueError, self.r1.update, id=80, width=0, x=17)
        self.assertRaises(ValueError, self.r1.update, id=80, width=-2,
                          height=5, x=5)

    def test_update_height_with_kwargs(self):
        self.r1.update(id=80)
        self.r3.update(id=82)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r3.height, 4)

        self.r1.update(id=80, width=2)
        self.r3.update(id=82, width=2)
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r3.height, 4)

        self.r1.update(id=80, width=2, height=3)
        self.r3.update(id=82, width=2, height=3)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r3.height, 3)

        self.r1.update(id=80, width=2, height=3, x=4)
        self.r3.update(id=82, width=2, height=3, x=4)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r3.height, 3)

        self.r1.update(id=80, width=2, height=3, x=4, y=5)
        self.r3.update(id=82, width=2, height=3, x=4, y=5)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r3.height, 3)

        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height="2")
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=[], x=3)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=(1, ), x=3, y=4)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3.45, x=0, y=4)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height={1, 3}, x=15, y=-3)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height={}, x=2, y=7)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=None, x=None)
        self.assertRaises(ValueError, self.r1.update, id=80, width=2,
                          height=0, x=17)
        self.assertRaises(ValueError, self.r1.update, id=80, width=2,
                          height=-2, x=5, y=5)

    def test_update_x_with_kwargs(self):
        self.r1.update(id=80)
        self.r3.update(id=82)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r3.x, 2)

        self.r1.update(id=80, width=2)
        self.r3.update(id=82, width=2)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r3.x, 2)

        self.r1.update(id=80, width=2, height=3)
        self.r3.update(id=82, width=2, height=3)
        self.assertEqual(self.r1.x, 0)
        self.assertEqual(self.r3.x, 2)

        self.r1.update(id=80, width=2, height=3, x=4)
        self.r3.update(id=82, width=2, height=3, x=4)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r3.x, 4)

        self.r1.update(id=80, width=2, height=3, x=4, y=5)
        self.r3.update(id=82, width=2, height=3, x=4, y=5)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r3.x, 4)

        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x="2")
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=[], y=3)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=(1, ), y=3)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=3.45, y=0)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x={1, 3}, y=15)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x={})
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=None, y=None)
        self.assertRaises(ValueError, self.r1.update, id=80, width=2,
                          height=3, x=-5, y=17)

    def test_update_y_with_kwargs(self):
        self.r1.update(id=80)
        self.r3.update(id=82)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)

        self.r1.update(id=80, width=2)
        self.r3.update(id=82, width=2)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)

        self.r1.update(id=80, width=2, height=3)
        self.r3.update(id=82, width=2, height=3)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)

        self.r1.update(id=80, width=2, height=3, x=4)
        self.r3.update(id=82, width=2, height=3, x=4)
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r3.y, 2)

        self.r1.update(id=80, width=2, height=3, x=4, y=5)
        self.r3.update(id=82, width=2, height=3, x=4, y=5)
        self.assertEqual(self.r1.y, 5)
        self.assertEqual(self.r3.y, 5)

        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=4, y="2")
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=4, y=[])
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=4, y=(1, ))
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=4, y=3.45)
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=4, y={1, 3})
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=4, y={})
        self.assertRaises(TypeError, self.r1.update, id=80, width=2,
                          height=3, x=4, y=None)
        self.assertRaises(ValueError, self.r1.update, id=80, width=2,
                          height=3, x=17, y=-5)

    def test_update_too_many_args(self):
        self.assertRaises(IndexError, self.r1.update, 80, 2, 3, 4, 5, 6, 7)

    def test_update_no_arg_or_kwarg(self):
        self.assertRaises(IndexError, self.r1.update)
        self.assertRaises(IndexError, self.r3.update)

    def test_update_invalid_kwargs(self):
        self.assertRaises(KeyError, self.r1.update, length=5)
        self.assertRaises(KeyError, self.r3.update, id=51, length=5, x=7)

    def test_update_kwargs_no_order(self):
        self.r1.update(width=2, y=5, height=3, id=80, x=4)
        self.assertEqual(self.r1.id, 80)
        self.assertEqual(self.r1.width, 2)
        self.assertEqual(self.r1.height, 3)
        self.assertEqual(self.r1.x, 4)
        self.assertEqual(self.r1.y, 5)

    def test_to_dictionary(self):
        rect1 = Rectangle(5, 5, 5, 5, 71)
        rect2 = Rectangle(10, 10, id=40)

        self.assertEqual(rect1.to_dictionary(), {
            'id': 71,
            'x': 5,
            'height': 5,
            'y': 5,
            'width': 5
        })
        self.assertEqual(rect2.to_dictionary(), {
            'id': 40,
            'x': 0,
            'height': 10,
            'y': 0,
            'width': 10
        })

        rect2.update(**rect1.to_dictionary())
        self.assertEqual(rect2.to_dictionary(), {
            'id': 71,
            'x': 5,
            'height': 5,
            'y': 5,
            'width': 5
        })
