import unittest
from rectangle import Rectangle
from square import Square


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


class TestSquare(unittest.TestCase):
    def test_compute_area(self):
        square = Square(5)
        self.assertEqual(square.compute_area(), 25)

    def test_set_side(self):
        square = Square(5)
        square.set_side(10)
        self.assertEqual(square.get_side(), 10)