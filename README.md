# Geometry Package

Geometry Package is a Python library for dealing with a handful of geometric tasks.

## Installation

Clone the repository:

```
git clone https://github.com/thomasha1310/geometry-package.git
cd geometry-package
```

Use pip to create an editable installation:

```
pip install -e .
```

## Usage

```python
from geometry import Circle, Square, Rectangle, area_stats

# Construct a square with side length 4:
square = Square(4)

# Shapes can also have non-integer side lengths:
rectangle = Rectangle(6.5, 3)

# Construct a circle:
circle = Circle(3.2)

# Print the area of the circle:
print(circle.area())

# Print a summary of the areas of all three shapes:
print(area_stats(square, rectangle, circle))
```

## License

This project is licensed under the [MIT License](LICENSE).
