from typing import Protocol
import math

class Shape(Protocol):
    def shape_area(self) -> float:
        pass

    def shape_perimeter(self) -> float:
        pass


class Rectangle:
    def __init__(self, side1: float, side2: float):
        self.side1 = side1
        self.side2 = side2

    def shape_area(self) -> float:
        return self.side1 * self.side2
    
    def shape_perimeter(self) -> float:
        return (self.side1 + self.side2) * 2
    

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def shape_area(self) -> float:
        return math.pi * self.radius **2
    
    def shape_perimeter(self) -> float:
        return 2 * math.pi * self.radius


def main():
    rect = Rectangle(5,4)
    circ = Circle(3)

    # pre-set sides and radius

    print("Rectangle: ")
    print("Area: ", rect.shape_area())
    print("Perimeter: ", rect.shape_perimeter())

    print("Circle:")
    print("Area: ", circ.shape_area())
    print("Perimeter: ", circ.shape_perimeter())

    # this is the main thart runs the functions


if __name__=='__main__':
    main()