import turtle

for x in range(3):
    turtle.right(20)
    for x in range (4):
        turtle.forward(100)
        turtle.right(90)

turtle.penup()
turtle.right(90)
turtle.forward(200)
turtle.pendown()

for x in range(12):
    turtle.right(360)
    for x in range(4):
        turtle.forward(100)
        turtle.right(60)






turtle.exitonclick()