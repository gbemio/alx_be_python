import math

class Shape:
    """Base class representing a geometric shape."""

    def area(self):
        """Method to calculate area. Must be overridden in subclasses."""
        raise NotImplementedError("Subclasses must override the area() method")


class Rectangle(Shape):
    """Derived class representing a rectangle."""

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Override area() to calculate rectangle area."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""

    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Override area() to calculate circle area."""
        return math.pi * (self.radius ** 2)
