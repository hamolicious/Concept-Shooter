from math import sqrt

class Vector():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def normalise(self):
        # mag = sqrt((dx * dx) + (dy * dy))

        # dx /= mag
        # dy /= mag

        mag = sqrt((self.x**2) + (self.y**2))
        self.div(mag)

    def add(self, other):
        if type(other) == Vector:
            self.x += other.x
            self.y += other.y

    def sub(self, other):
        if type(other) == Vector:
            self.x -= other.x
            self.y -= other.y
    
    def __sub__(self, other):
        if type(other) == Vector:
            return Vector(self.x - other.x, self.y - other.y)
    
    def mult(self, other):
        if type(other) == Vector:
            self.x *= other.x
            self.y *= other.y
        elif type(other) in [int, float]:
            self.x *= other
            self.y *= other

    def div(self, other):
        if type(other) == Vector:
            self.x /= other.x
            self.y /= other.y
        elif type(other) in [int, float]:
            self.x /= other
            self.y /= other
            