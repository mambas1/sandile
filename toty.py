import turtle
def draw_triangle(side1, int_angle, side2):
    turn_angle=180-int_angle
    turtle.forward(side1)
    turtle.left(turn_angle)
    turtle.forward(side2)
    turtle.home()
draw_triangle(100,100,150)
turtle.done()

import turtle
def draw_parallelogram(side1, side2,int_angle1):
    turn_angle1 = 180-int_angle1
    i=0;
    while (i < 2):
        turtle.fd(side1)
        turtle.lt(turn_angle1)
        turtle.fd(side2)
        turtle.lt(int_angle1)
        i=i+1
draw_parallelogram(100,150,120)
turtle.done()

import turtle
def draw_circle(radius):
    turtle.circle(radius)
draw_circle(100)
turtle.done()

