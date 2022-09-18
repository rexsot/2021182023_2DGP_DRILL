import turtle
count = 6
turtle.penup()
turtle.goto(250,250)
turtle.right(90)
while (count > 0):
    turtle.pendown()
    turtle.forward(500)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(180)
    count -= 1
turtle.goto(-250,250)
turtle.left(90)
count = 6
while (count > 0):
    turtle.pendown()
    turtle.forward(500)
    turtle.right(90)
    turtle.penup()
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(500)
    turtle.right(180)
    count -= 1

