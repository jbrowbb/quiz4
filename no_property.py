class Rectanlge:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def get_width(self):
        return self._width
    
    def set_width(self, value):
        if value <= 0:
            raise ValueError("Width must be a positive member")
        
        self._width = value

    def get_height(self):
        return self._height
    
    def set_height(self, value):
        if value <= 0:
            raise ValueError("Height must be a positive number")
        
        self._height = value

    def area(self):
        return self.get_width() * self.get_height()
    
    def perimeter(self):
        return 2 * (self.get_width() + self.get_height())
    

def main():
    rectangle = Rectanlge(5,3)

    print("Width 1: ", rectangle.get_width())
    print("Height 1: ", rectangle.get_height())
    print("Area: ", rectangle.area())
    print("Perimeter: ", rectangle.perimeter())

    rectangle.set_width(7)
    rectangle.set_height(4)

    print("Width 2: ", rectangle.get_width())
    print("Height 2: ", rectangle.get_height())
    print("Area: ", rectangle.area())
    print("Perimeter: ", rectangle.perimeter())


if __name__=='__main__':
    main()