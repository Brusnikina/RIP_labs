from Rectangle import Rectangle
from Square import Square
from Circle import Circle

if __name__ == "__main__":
    rec = Rectangle(3, 2, 'blue')
    cir = Circle(5, 'green')
    sq = Square(5, 'red')
    print(rec.__repr__())
    print(cir.__repr__())
    print(sq.__repr__())
