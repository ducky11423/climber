# main.py - entry point and setup

import graphics

win = graphics.GraphWin("Climb", 1280, 720)
circ = graphics.Circle(graphics.Point(1280/2, 720/2), 100)
circ.draw(win)









win.getMouse()
win.close()