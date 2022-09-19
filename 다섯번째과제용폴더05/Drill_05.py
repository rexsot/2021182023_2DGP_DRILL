import turtle
import random

turtle.shape('turtle')

def w_move():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def a_move():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()

def s_move():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()

def d_move():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()


turtle.onkey(w_move, 'w')
turtle.onkey(a_move, 'a')
turtle.onkey(s_move, 's')
turtle.onkey(d_move, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()
