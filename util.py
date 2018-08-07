# util.py - various classes to make my life better

import math

class Vector:
    def __init__(self, x = 0, y = 0, vector = None):
        if vector is not None:
            self.x = vector.x
            self.y = vector.y
        else:
            self.x = x
            self.y = y

    def mag(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def mag_sqr(self):
        return (self.x * self.x + self.y * self.y)

    def add(self, vec):
        self.x += vec.x
        self.y += vec.y

        return self

    def scale(self, scalar: float):
        self.x *= scalar
        self.y *= scalar

        return self

    def norm(self):
        # note: this is destructive (aka it destroys the vector)
        mag = self.mag()
        return self.scale(1/mag)
