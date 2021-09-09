import turtle

def drawhouse():
    for x in range(4):
        turtle.forward(100)
        turtle.right(90)
    for x in range (3):
        turtle.forward(100)
        turtle.right(120)

drawhouse()






turtle.exitonclick()