# Класс "Квадрат"
from Rectangle import Rectangle
from Color import Color


class Square(Rectangle):
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, a, color):
        self.a = a
        super().__init__(a, a, color)

    def __repr__(self):
        return '{} {} цвета со сторонами {} и площадью {}'.format(
            Square.get_figure_type(),
            self.color.colorprop,
            self.a,
            self.square()
        )
