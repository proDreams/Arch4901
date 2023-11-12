# Переписать код в соответствии с Liskov Substitution Principle:

class Shape:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def set_dimensions(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Rectangle(Shape):
    def set_dimensions(self, width, height):
        super().set_dimensions(width, height)


class Square(Shape):
    def set_dimensions(self, side):
        super().set_dimensions(side, side)
