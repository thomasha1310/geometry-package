from geometry import Circle, Square, area_stats

# Construct a square with side length 4:
square = Square(4)

# Shapes can also have non-integer side lengths:
square2 = Square(6.4)

# Construct a circle:
circle = Circle(3.2)

# Print the area of the circle:
print(circle.area())

# Print a summary of the areas of all three shapes:
print(area_stats(square, square2, circle))