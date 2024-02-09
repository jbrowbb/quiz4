# Quiz 4

arguments.py
    * Write a python program argparse module with three inputs, stig, int, float
    * Example >> python3 arguments.py hello 007 9.11

abc_classes.py
    * Write a program to demonstrate ABC
    * Created a base class called Shape(ABC)
    * Two abstract methods in Shape using abstractmethod decorator, shape_area(self) and shape_perimeter(self), passing both
    * Base class is inherited by tow other classes, Rectangle(Shape) and Circle(Shape)
    * Implement the methods inside of the base class
    * Pre-set functions in main and print out the classes methods

protocol.py
    * Rewrite abc_classes.py ising the protocol method

dataclass.py
    * Write a program in which the class is using @dataclass decorator
    * Used class Product

dataclass_ext.py
    * Extend dataclass.py to include an extra funtion inside of the @dataclass class
    * Inside Product def info_display(self) -> None

property.py
    * Write a program that will demonstrate the @property decorator
    * class Rectangle
    * @property with width, then @width.setter. Same with height
    * @property with area and perimeter

no_property.py
    * Extend property.py by removing the @property decorator
    * Use self._ to append width and height to self

run.py
    * Write a program that uses functions from different python files
    * Functions: dimensin.py, volume.py, and surface_area.py