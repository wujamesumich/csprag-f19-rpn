import unittest
import rpn

# create class called TestBasics, but inherit from unittest
# class inside of unittest called TestCase
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        # self ~= this in C++
        self.assertEqual(2, result)
