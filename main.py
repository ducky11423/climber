# main.py - entry point and setup

import graphics
from climber import Climber

win = graphics.GraphWin("Climb", 1280, 720)
win.setCoords(-20, -2.5, 20, 20) # TODO: make this better

climber = Climber()
drawObjects = climber.get_draw()

for obj in drawObjects:
    obj.draw(win)

win.getMouse()
win.close()