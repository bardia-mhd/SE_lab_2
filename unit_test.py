import unittest
from rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_compute_area(self):
        rectangle = Rectangle(5, 7)
        self.assertEqual(rectangle.compute_area(), 35)
