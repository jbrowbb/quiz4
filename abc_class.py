from abc import ABC, abstractmethod
import math

class Shape(ABC):
    
    @abstractmethod
    def shape_area(self):
        pass

    @abstractmethod
    def shape_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2
        # init side1 & side2

    def shape_area(self):
        return self.side1 * self.side2
        # returns the shape area
    
    def shape_perimeter(self):
        return (self.side1 + self.side2) * 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        # init radius to self

    def shape_area(self):
        return math.pi * self.radius ** 2
    
    def shape_perimeter(self):
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