class ShapeDimensions:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def set_dimensions(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_dimesions(self):
        return self.length, self.width, self.height