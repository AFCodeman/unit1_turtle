import turtle

def drawoctogon(color):
    turtle.pencolor(color)
    turtle.begin_fill()
    turtle.fillcolor(color)
    for x in range(8):
        turtle.forward(100)
        turtle.right(45)
    turtle.end_fill()

def octogongo(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()


drawoctogon("violet")

octogongo(200,200)

drawoctogon("red")

octogongo(200,-200)

drawoctogon("green")

octogongo(-200,200)

drawoctogon("orange")

octogongo(-200,-200)

turtle.exitonclick()