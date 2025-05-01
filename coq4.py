import math

class RegularShape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return NotImplemented

    def perimeter(self):
        return NotImplemented


class Square(RegularShape):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


class Circle(RegularShape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class EquilateralTriangle(RegularShape):
    def __init__(self, side):
        super().__init__("Equilateral Triangle")
        self.side = side

    def area(self):
        return (math.sqrt(3) / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side



shapes = [
    Square(5),
    Circle(3),
    EquilateralTriangle(6)
]

for shape in shapes:
    print(f"{shape.name}:")
    print(f"  Area = {shape.area():.2f}")
    print(f"  Perimeter = {shape.perimeter():.2f}\n")
