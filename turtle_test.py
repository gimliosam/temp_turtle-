from Tkinter import *
from turtle import *
import turtle

def default_triangle_arg( side_length ):
    fd(side_length)
    rt(120)
    fd(side_length)
    rt(120)
    fd(side_length)
    rt(120)

# Teleports the turtle to the opposite side of the screen 
#    if the turtle falls off the screen 
def wrap_check(): 
    if xcor() < left or xcor() > right:
        setx( xcor() * -1)
    if ycor() < bottom or ycor() > top: 
        sety( ycor() * -1)




mode('logo')

# 330, 238
turtle.setup(660, 475)
screen = turtle.Screen()
screenWidth = screen.window_width()
screenHeight = screen.window_height() 

left = -1 * screenWidth/2
right = screenWidth / 2
top = screenHeight / 2 
bottom = -1 * screenHeight / 2 


default_triangle_arg(100)
default_triangle_arg(10)

hideturtle()

# speed 1 slowest.... 5 medium .... 10 fast ... 0 fastest ... weird so I left a comment :) 
speed(0)

# This is how we make a "variable" called side_length and "assigned" 100
side_length = 100

# don't worry about this, but leave this and update() in for speed :) 
#tracer(0, 0)



pensize(0.2)

# This is a loop in python... like "repeat" in logo... 
for x in range(12000):
    default_triangle_arg(side_length)
    pu() 
    fd(10)
    rt(2)
    pd() 

    wrap_check()

    side_length = side_length - 1
    print x
    print xcor() 
    print ycor()


# don't worry about this, but leave this and update() in for speed :) 
#update()

ts = turtle.getscreen()
ts.getcanvas().postscript(file="pic.ps")

done()