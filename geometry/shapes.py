from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Compute the area of the shape."""
        
class Square(Shape):
    def __init__(self, side: float):
        if not isinstance(side, (int, float)):
            raise ValueError("Side length must be numeric.")
        super().__init__()
        self.side = side
    
    def area(self) -> float:
        if (self.side < 0):
            raise ValueError("Side length must be non-zero to calculate area.")
        return self.side ** 2
    
class Circle(Shape):
    def __init__(self, radius: float):
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius length must be numeric.")
        super().__init__()
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2