import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

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
