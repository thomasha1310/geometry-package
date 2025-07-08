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