def area_stats(*shapes):
    if len(shapes) == 0:
        raise ValueError("At least one Shape is required.")
    
    areas = [shape.area() for shape in shapes]
    return {
        "n": len(areas),
        "total": sum(areas),
        "mean": sum(areas) / len(areas),
        "min": min(areas),
        "max": max(areas)
    }