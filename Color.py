# Класс "Цвет фигуры"


class Color:
    def __init__(self):
        self._color = None

    @property
    def colorprop(self):
        return self._color

    @colorprop.setter
    def colorprop(self, new_color):
        self._color = new_color
