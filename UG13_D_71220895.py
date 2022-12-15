import turtle

pen = turtle.Turtle()

# hutuf D
def hurufD(x, y, z):
    pen.up()
    pen.goto(x, y)
    pen.down()
    pen.pencolor("light green")
    pen.pensize(9)
    for i in range(1):
        pen.forward(100)
        pen.circle(100, 90)
        pen.forward(50)
        pen.circle(100, 90)
        pen.forward(100)
        pen.left(90)
        pen.forward(250)

hurufD(0, 0, 100)

sc = turtle.Screen().exitonclick()