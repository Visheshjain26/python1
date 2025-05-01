import math

class Solid:
    def __init__(self, height=None, length=None, breadth=None):
        self.height = height
        self.length = length
        self.breadth = breadth


class Cube(Solid):
    def __init__(self, length):
        super().__init__(length=length)
        self.length = length

    def area(self):
        return 6 * (self.length ** 2)

    def volume(self):
        return self.length ** 3


class Cuboid(Solid):
    def __init__(self, length, breadth, height):
        super().__init__(height=height, length=length, breadth=breadth)

    def area(self):
        return 2 * (self.length*self.breadth + self.breadth*self.height + self.height*self.length)

    def volume(self):
        return self.length * self.breadth * self.height


class Cylinder(Solid):
    def __init__(self, radius, height):
        super().__init__(height=height)
        self.radius = radius

    def area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self):
        return math.pi * self.radius ** 2 * self.height


class Cone(Solid):
    def __init__(self, radius, height, slant_height):
        super().__init__(height=height)
        self.radius = radius
        self.slant_height = slant_height

    def area(self):
        return math.pi * self.radius * (self.radius + self.slant_height)

    def volume(self):
        return (1/3) * math.pi * self.radius ** 2 * self.height


class Sphere(Solid):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        return (4/3) * math.pi * self.radius ** 3

class Hemisphere(Solid):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3 * math.pi * self.radius ** 2

    def volume(self):
        return (2/3) * math.pi * self.radius ** 3
