import pytest

from geometry import Square, Circle, area_stats

def test_square_area_zero_and_positive():
    square = Square(0.0)
    assert square.area() == pytest.approx(0.0)
    
    square = Square(1.1)
    assert square.area() == pytest.approx(1.21)
    
    with pytest.raises(ValueError):
        square = Square(-5.2)
        square.area()
    
def test_stats_keys_and_values():
    square = Square(5)
    circle = Circle(3)
    stats = area_stats(square, circle)
    assert isinstance(stats, dict)
    assert list(stats.keys()) == ["n", "total", "mean", "min", "max"]
    assert all(isinstance(v, (int, float)) for v in stats.values())

def test_stats_raises_without_states():
    with pytest.raises(ValueError):
        area_stats()