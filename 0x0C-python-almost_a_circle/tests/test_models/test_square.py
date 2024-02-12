import sys
from io import StringIO
import unittest
from models.square import Square


class TestSquareId(unittest.TestCase):

    def test_square_instance_id(self):
        sq1 = Square(10, 2, 2, 33)
        sq2 = Square(8, 3, 4, 34)

        self.assertEqual(sq1.id, 33)
        self.assertEqual(sq2.id, 34)


class TestSquareObj(unittest.TestCase):

    def setUp(self):
        self.s1 = Square(10, 2)
        self.s2 = Square(2, 10)
        self.s3 = Square(5, 2, 2, 12)

    def tearDown(self):
        pass

    def test_size(self):
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s2.size, 2)
        self.assertEqual(self.s3.size, 5)
        self.s1.size = 15
        self.assertEqual(self.s1.size, 15)
        self.assertRaises(TypeError, Square, "5", 4)
        square = Square(3, 3)
        self.assertRaises(TypeError, setattr, square, "size", "4")
        self.assertRaises(TypeError, setattr, square, "size", [])
        self.assertRaises(TypeError, setattr, square, "size", None)
        self.assertRaises(TypeError, setattr, square, "size", {})
        self.assertRaises(TypeError, setattr, square, "size", {1, 2})
        self.assertRaises(TypeError, setattr, square, "size", 3.15)
        self.assertRaises(TypeError, setattr, square, "size", (1, ))
        self.assertRaises(ValueError, setattr, square, "size", 0)
        self.assertRaises(ValueError, setattr, square, "size", -5)

    def test_x_coordinate(self):
        self.assertEqual(self.s1.x, 2)
        self.assertEqual(self.s2.x, 10)
        self.assertEqual(self.s3.x, 2)
        self.s1.x = 15
        self.assertEqual(self.s1.x, 15)
        self.assertRaises(TypeError, Square, 5, "2", 2, 151)
        square = Square(3, 3)
        self.assertRaises(TypeError, setattr, square, "x", "4")
        self.assertRaises(TypeError, setattr, square, "x", [])
        self.assertRaises(TypeError, setattr, square, "x", None)
        self.assertRaises(TypeError, setattr, square, "x", {})
        self.assertRaises(TypeError, setattr, square, "x", {1, 2})
        self.assertRaises(TypeError, setattr, square, "x", 3.15)
        self.assertRaises(TypeError, setattr, square, "x", (1, ))
        self.assertRaises(ValueError, setattr, square, "x", -5)

    def test_y_coordinate(self):
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 0)
        self.assertEqual(self.s3.y, 2)
        self.s1.y = 15
        self.assertEqual(self.s1.y, 15)
        self.assertRaises(TypeError, Square, 5, 2, "2", 152)
        square = Square(3, 3)
        self.assertRaises(TypeError, setattr, square, "y", "4")
        self.assertRaises(TypeError, setattr, square, "y", [])
        self.assertRaises(TypeError, setattr, square, "y", None)
        self.assertRaises(TypeError, setattr, square, "y", {})
        self.assertRaises(TypeError, setattr, square, "y", {1, 2})
        self.assertRaises(TypeError, setattr, square, "y", 3.15)
        self.assertRaises(TypeError, setattr, square, "y", (1, ))
        self.assertRaises(ValueError, setattr, square, "y", -5)

    def test_area(self):
        self.assertEqual(self.s1.area(), 100)
        self.assertEqual(self.s2.area(), 4)
        self.assertEqual(self.s3.area(), 25)
        self.s1.size = 15
        self.assertEqual(self.s1.area(), 225)

    def test_str_(self):
        square1 = Square(4, 2, 1, 12)
        square2 = Square(10, id=54)

        self.assertEqual(str(square1), "[Square] (12) 2/1 - 4")
        self.assertEqual(str(square2), "[Square] (54) 0/0 - 10")

    def test_display(self):
        square1 = Square(2, 1, 1, 57)
        captured_output = StringIO()
        sys.stdout = captured_output

        square1.display()
        printed = captured_output.getvalue()

        sys.stdout = sys.__stdout__
        self.assertEqual(printed, "\n ##\n ##\n")

    def test_update_id_with_args(self):
        square1 = Square(5, 5, 5, 71)
        square2 = Square(10, 10)

        square1.update(80)
        square2.update(82)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

        square1.update(80, 2)
        square2.update(82, 2)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

        square1.update(80, 2, 4)
        square2.update(82, 2, 4)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

        square1.update(80, 2, 4, 5)
        square2.update(82, 2, 4, 5)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

    def test_update_size_with_args(self):
        self.s1.update(80)
        self.s3.update(82)
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s3.size, 5)

        self.s1.update(80, 2)
        self.s3.update(82, 2)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s3.size, 2)

        self.s1.update(80, 2, 4)
        self.s3.update(82, 2, 4)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s3.size, 2)

        self.s1.update(80, 2, 4, 5)
        self.s3.update(82, 2, 4, 5)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s3.size, 2)

        self.assertRaises(TypeError, self.s1.update, 80, "2")
        self.assertRaises(TypeError, self.s1.update, 80, [], 3)
        self.assertRaises(TypeError, self.s1.update, 80, (1, ), 3, 4)
        self.assertRaises(TypeError, self.s1.update, 80, 3.45, 0, 4)
        self.assertRaises(TypeError, self.s1.update, 80, {1, 3}, 15, -3)
        self.assertRaises(TypeError, self.s1.update, 80, {}, 1, 2)
        self.assertRaises(TypeError, self.s1.update, 80, None, None, None)
        self.assertRaises(ValueError, self.s1.update, 80, 0, 17)
        self.assertRaises(ValueError, self.s1.update, 80, -2, 5, 5)

    def test_update_x_with_args(self):
        sq1 = Square(10, 2)
        sq3 = Square(5, 2, 2, 12)

        sq1.update(80)
        sq3.update(82)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq3.x, 2)

        sq1.update(80, 2)
        sq3.update(82, 2)
        self.assertEqual(sq1.x, 2)
        self.assertEqual(sq3.x, 2)

        sq1.update(80, 2, 4)
        sq3.update(82, 2, 4)
        self.assertEqual(sq1.x, 4)
        self.assertEqual(sq3.x, 4)

        sq1.update(80, 2, 4, 5)
        sq3.update(82, 2, 4, 5)
        self.assertEqual(sq1.x, 4)
        self.assertEqual(sq3.x, 4)

        self.assertRaises(TypeError, self.s1.update, 80, 2, "2")
        self.assertRaises(TypeError, self.s1.update, 80, 2, [], 3)
        self.assertRaises(TypeError, self.s1.update, 80, 2, (1, ), 3)
        self.assertRaises(TypeError, self.s1.update, 80, 2, 3.45, 0)
        self.assertRaises(TypeError, self.s1.update, 80, 2, {1, 3}, 15)
        self.assertRaises(TypeError, self.s1.update, 80, 2, {})
        self.assertRaises(TypeError, self.s1.update, 80, 2, None, None)
        self.assertRaises(ValueError, self.s1.update, 80, 2, -5, 17)

    def test_update_y_with_args(self):
        self.s1.update(80)
        self.s3.update(82)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 2)

        self.s1.update(80, 2)
        self.s3.update(82, 2)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 2)

        self.s1.update(80, 2, 4)
        self.s3.update(82, 2, 4)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 2)

        self.s1.update(80, 2, 4, 5)
        self.s3.update(82, 2, 4, 5)
        self.assertEqual(self.s1.y, 5)
        self.assertEqual(self.s3.y, 5)

        self.assertRaises(TypeError, self.s1.update, 80, 2, 4, "2")
        self.assertRaises(TypeError, self.s1.update, 80, 2, 4, [])
        self.assertRaises(TypeError, self.s1.update, 80, 2, 4, (1, ))
        self.assertRaises(TypeError, self.s1.update, 80, 2, 4, 3.45)
        self.assertRaises(TypeError, self.s1.update, 80, 2, 4, {1, 3})
        self.assertRaises(TypeError, self.s1.update, 80, 2, 4, {})
        self.assertRaises(TypeError, self.s1.update, 80, 2, 4, None)
        self.assertRaises(ValueError, self.s1.update, 80, 2, 17, -5)

    def test_update_id_with_kwargs(self):
        square1 = Square(5, 5, 5, 71)
        square2 = Square(10, 10)

        square1.update(id=80)
        square2.update(id=82)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

        square1.update(id=80, size=2)
        square2.update(id=82, size=2)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

        square1.update(id=80, size=2)
        square2.update(id=82, size=2)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

        square1.update(id=80, size=2, x=4)
        square2.update(id=82, size=2, x=4)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

        square1.update(id=80, size=2, x=4, y=5)
        square2.update(id=82, size=2, x=4, y=5)
        self.assertEqual(square1.id, 80)
        self.assertEqual(square2.id, 82)

    def test_update_size_with_kwargs(self):
        self.s1.update(id=80)
        self.s3.update(id=82)
        self.assertEqual(self.s1.size, 10)
        self.assertEqual(self.s3.size, 5)

        self.s1.update(id=80, size=2)
        self.s3.update(id=82, size=2)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s3.size, 2)

        self.s1.update(id=80, size=2)
        self.s3.update(id=82, size=2, )
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s3.size, 2)

        self.s1.update(id=80, size=2, x=4)
        self.s3.update(id=82, size=2, x=4)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s3.size, 2)

        self.s1.update(id=80, size=2, x=4, y=5)
        self.s3.update(id=82, size=2, x=4, y=5)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s3.size, 2)

        self.assertRaises(TypeError, self.s1.update, id=80, size="2")
        self.assertRaises(TypeError, self.s1.update, id=80, size=[], x=3)
        self.assertRaises(TypeError, self.s1.update, id=80, size=(1, ),
                          x=4)
        self.assertRaises(TypeError, self.s1.update, id=80, size=3.45, x=0,
                          y=4)
        self.assertRaises(TypeError, self.s1.update, id=80, size={1, 3},
                          y=15, x=-3)
        self.assertRaises(TypeError, self.s1.update, id=80, size={},
                          x=2, y=7)
        self.assertRaises(TypeError, self.s1.update, id=80, size=None, x=None)
        self.assertRaises(ValueError, self.s1.update, id=80, size=0, x=17)
        self.assertRaises(ValueError, self.s1.update, id=80, size=-2,
                          x=5)

    def test_update_x_with_kwargs(self):
        self.s1.update(x=4)
        self.s3.update(x=4)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s3.x, 4)

        self.s1.update(id=80, size=2)
        self.s3.update(id=82, size=2)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s3.x, 4)

        self.s1.update(id=80, size=2, x=4)
        self.s3.update(id=82, size=2, x=4)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s3.x, 4)

        self.s1.update(id=80, size=2, x=4, y=5)
        self.s3.update(id=82, size=2, x=4, y=5)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s3.x, 4)

        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x="2")
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=[], y=3)
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=(1, ), y=3)
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=3.45, y=0)
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x={1, 3}, y=15)
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x={})
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=None, y=None)
        self.assertRaises(ValueError, self.s1.update, id=80, size=2,
                          x=-5, y=17)

    def test_update_y_with_kwargs(self):
        self.s1.update(id=80)
        self.s3.update(id=82)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 2)

        self.s1.update(id=80, size=2)
        self.s3.update(id=82, size=2)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 2)

        self.s1.update(id=80, size=2, )
        self.s3.update(id=82, size=2, )
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 2)

        self.s1.update(id=80, size=2, x=4)
        self.s3.update(id=82, size=2, x=4)
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s3.y, 2)

        self.s1.update(id=80, size=2, x=4, y=5)
        self.s3.update(id=82, size=2, x=4, y=5)
        self.assertEqual(self.s1.y, 5)
        self.assertEqual(self.s3.y, 5)

        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=4, y="2")
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=4, y=[])
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=4, y=(1, ))
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=4, y=3.45)
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=4, y={1, 3})
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=4, y={})
        self.assertRaises(TypeError, self.s1.update, id=80, size=2,
                          x=4, y=None)
        self.assertRaises(ValueError, self.s1.update, id=80, size=2,
                          x=17, y=-5)

    def test_update_too_many_args(self):
        self.assertRaises(IndexError, self.s1.update, 80, 2, 4, 5, 6, 7)

    def test_update_no_arg_or_kwarg(self):
        self.assertRaises(IndexError, self.s1.update)
        self.assertRaises(IndexError, self.s3.update)

    def test_update_invalid_kwargs(self):
        self.assertRaises(KeyError, self.s1.update, length=5)
        self.assertRaises(KeyError, self.s3.update, id=51, length=5, x=7)

    def test_update_kwargs_no_order(self):
        self.s1.update(size=2, y=5, id=80, x=4)
        self.assertEqual(self.s1.id, 80)
        self.assertEqual(self.s1.size, 2)
        self.assertEqual(self.s1.x, 4)
        self.assertEqual(self.s1.y, 5)

    def test_to_dictionary(self):
        sq1 = Square(5, 5, 5, 71)
        sq2 = Square(10, id=40)

        self.assertEqual(sq1.to_dictionary(), {
            'id': 71,
            'x': 5,
            'y': 5,
            'size': 5
        })
        self.assertEqual(sq2.to_dictionary(), {
            'id': 40,
            'x': 0,
            'y': 0,
            'size': 10
        })

        sq2.update(**sq1.to_dictionary())
        self.assertEqual(sq2.to_dictionary(), {
            'id': 71,
            'x': 5,
            'y': 5,
            'size': 5
        })
