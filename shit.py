import turtle

window = turtle.Screen()
window.bgcolor("black")
shapeA = turtle.Turtle()
shapeB = turtle.Turtle()
shapeC = turtle.Turtle()
shapeD = turtle.Turtle()

shapeA.sety(100)
shapeA.pencolor("red")
for i in range(3):
    shapeA.pensize(3)
    shapeA.fd(50)
    shapeA.left(120)

shapeB.setx(-100)
shapeB.pencolor("blue")
for i in [1, 2, 3, 4]:
    shapeB.pensize(3)
    shapeB.fd(50)
    shapeB.right(90)

shapeC.pencolor("purple")
shapeC.pensize(3)
shapeC.circle(30)

shapeD.setx(25)
shapeD.sety(-25)
shapeD.pencolor("yellow")
shapeD.pensize(3)
shapeD.fd(100)

window.exitonclick()
