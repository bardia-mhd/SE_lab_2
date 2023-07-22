from shape import Shape

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def set_side(self, side):
        self.side = side

    def get_side(self):
        return self.side

    def compute_area(self):
        return self.side ** 2