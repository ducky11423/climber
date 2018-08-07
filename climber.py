# climber.py - class for the object which actually climbs. will be fed input from nn

import graphics
from util import *

class Node:
    def __init__(self, x, y):
        self.pos = Vector(x, y)

    @property
    def x(self):
        return self.pos.x
    @x.setter
    def x(self, x):
        self.pos.x = x

    @property
    def y(self):
        return self.pos.y
    @y.setter
    def y(self, y):
        self.pos.y = y

    
    

class Climber:
    def __init__(self):
        self.node1 = Node(-0.5, 0.5) 
        self.node2 = Node(0.5, 0.5) # the two nodes of the climber
        self.length = 1 # the length of the bone connecting the two nodes

    def get_draw(self):
        # returns a list of objects which should be drawn to represent this creature. 

        draw = []
        
        draw.append(graphics.Circle(graphics.Point(self.node1.x, self.node1.y), 0.2))
        draw.append(graphics.Circle(graphics.Point(self.node2.x, self.node2.y), 0.2))
        draw.append(graphics.Line(graphics.Point(self.node1.x, self.node1.y), graphics.Point(self.node2.x, self.node2.y)))

        return draw