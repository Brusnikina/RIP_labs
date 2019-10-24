# Класс "Круг"
from Color import Color
from Figure import Figure
import math


class Circle(Figure):
    FIGURE_TYPE = "Круг"
    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, r, color):
        self.r = r
        self.color = Color()
        self.color.colorprop = color

    def square(self):
        return (self.r ** 2) * math.pi

    def __repr__(self):
        return '{} {} цвета, с радиусом {} и площадью {}'.format(
            Circle.get_figure_type(),
            self.color.colorprop,
            self.r,
            self.square()
        )