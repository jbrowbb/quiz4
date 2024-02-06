class Rectanlge:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive number")
        
        self._width = value

    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number")
        
        self._height = value

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def perimeter(self):
        return 2 * (self.width + self.height)
    

def main():
    rectangle = Rectanlge(5,3)

    print("Width 1: ", rectangle.width)
    print("Height 1: ", rectangle.height)
    print("Area: ", rectangle.area)
    print("Perimeter: ", rectangle.perimeter)

    rectangle.width = 7
    rectangle.height = 4

    print("Width 2: ", rectangle.width)
    print("Height 2: ", rectangle.height)
    print("Area: ", rectangle.area)
    print("Perimeter: ", rectangle.perimeter)


if __name__=='__main__':
    main()