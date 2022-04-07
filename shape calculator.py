class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, x):
        self.width = x

    def set_height(self, y):
        self.height = y

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return ((self.width ** 2) + (self.height ** 2)) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        lines_height = self.height
        lines_width = self.width
        s = (("*" * lines_width) + "\n") * lines_height
        return s

    def get_amount_inside(self, polygon):

        return self.get_area() // polygon.get_area()


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __str__(self):
        return f'Square(side={self.width})'

    def set_side(self, r):
        self.width = r
        self.height = r