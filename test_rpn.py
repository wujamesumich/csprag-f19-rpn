import unittest
import rpn

# create class called TestBasics, but inherit from unittest
# class inside of unittest called TestCase
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        # self ~= this in C++
        self.assertEqual(2, result)
    def test_sub(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)
    def test_badinput(self):
        with self.assertRaises(TypeError):
            rpn.calculate('1 2 3 +')
    # ADDED HW8
    def test_exp(self):
        result = rpn.calculate('5 3 ^')
        self.assertEqual(125, result)