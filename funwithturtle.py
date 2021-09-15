import turtle

def audilogo():
    turtle.width(10)
    for x in range(4):
        turtle.circle(100)
        turtle.penup()
        turtle.forward(130)
        turtle.pendown()

def bmwlogo():
    turtle.right(30)
    turtle.forward(100)
    turtle.right(165)
    turtle.forward(100)
    turtle.right(325)
    turtle.forward(100)
    turtle.right(165)
    turtle.forward(100)
    turtle.right(315)
    turtle.forward(100)
    turtle.right(165)
    turtle.forward(100)

    turtle.penup()
    turtle.right(255)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(12)
    turtle.pendown()
    turtle.circle(105)

bmwlogo()

turtle.exitonclick()