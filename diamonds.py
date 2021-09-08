import turtle

turtle.right(30)
for x in range(6):
    turtle.right(60)
    for x in range(6):
        turtle.forward(100)
        turtle.right(60)

turtle.exitonclick()