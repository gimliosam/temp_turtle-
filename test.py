from Tkinter import *
from turtle import *
import turtle

color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()


ts = turtle.getscreen()

ts.getcanvas().postscript(file="duck.eps")

done()