#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
    Defines test for 6-max_integer module
    """

    def test_max_integer(self):
        self.assertEqual(max_integer([4, 5, 6, 7]), 7)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

        with self.assertRaises(TypeError):
            max_integer(5)
            max_integer(None)
