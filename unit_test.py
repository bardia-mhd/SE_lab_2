import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_compute_area(self):
        rectangle = Rectangle(5, 7)
        self.assertEqual(rectangle.compute_area(), 35)

    def test_set_width(self):
        rectangle = Rectangle(5, 7)
        rectangle.set_width(10)
        self.assertEqual(rectangle.get_width(), 10)

    def test_set_height(self):
        rectangle = Rectangle(5, 7)
        rectangle.set_height(8)
        self.assertEqual(rectangle.get_height(), 8)
