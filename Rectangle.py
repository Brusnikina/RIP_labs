# Класс "Прямоугольник"
from Color import Color
from Figure import Figure


class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color()
        self.color.colorprop = color

    def square(self):
        return self.width * self.height

    def __repr__(self):
        return '{} {} цвета с шириной {}, высотой {} и площадью {}'.format(
            Rectangle.get_figure_type(),
            self.color.colorprop,
            self.height,
            self.width,
            self.square()
        )
