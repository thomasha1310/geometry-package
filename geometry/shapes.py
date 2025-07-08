from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Compute the area of the shape."""
        
class Square(Shape):
    def __init__(self, side: float):
        super().__init__()
        self.side = side
    
    def area(self) -> float:
        return self.side ** 2
    
class Circle(Shape):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2