import math

class Circle:
    def __init__(self, radius:float):
        self.radius = radius

    # The total space within the circle (in units squared, e.g. square inches)
    def get_area(self):
        return math.pi * self.radius * self.radius

    # The length of a straight line that passes through the circle's center
    def get_diameter(self):
        return self.radius * 2

    # The distance around the circle, the length of its perimeter
    def get_circumference(self):
        return math.pi * self.radius * 2

    def __eq__(self, o):
        if not isinstance(o, Circle):
            return False
        return self.radius == o.radius
