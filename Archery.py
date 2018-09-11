#CS1400
import turtle
#start execution
window = turtle.Screen()
window.setup(width=250, height=250, startx=None, starty=None)
shapeA = turtle.Turtle()
shapeB = turtle.Turtle()
shapeC = turtle.Turtle()
shapeD = turtle.Turtle()
shapeE = turtle.Turtle()
shapeF = turtle.Turtle()

shapeF.sety(-81)
shapeF.circle(81)

shapeE.pencolor("white")
shapeE.dot(160)

shapeD.pencolor("black")
shapeD.dot(120)

shapeC.pencolor("blue")
shapeC.dot(80)

shapeB.pencolor("red")
shapeB.dot(50)

shapeA.shape("circle")
shapeA.color("yellow")
#exit
window.exitonclick()
