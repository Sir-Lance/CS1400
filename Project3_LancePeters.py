#Lance Peters
#CS1400-003
#Programming Project #3: Farmer John's Field
#Oct, 6, 2018
import turtle

window = turtle.Screen()
windowTitle = "Project 3"
window.bgcolor("green")

c4 = turtle.Turtle()
c1 = turtle.Turtle()
sq = turtle.Turtle()

def drawSpeed():
    c4.speed(10)
    c1.speed(10)
    sq.speed(10)
drawSpeed()

def drawCircle1():
    c1.setpos(50, -50)
    c1.color("black", "grey")
    c1.begin_fill()
    c1.pensize(3)
    c1.circle(50)
    c1.end_fill()
drawCircle1()

def drawCircle4():
    c4.color("black", "white")
    c4.pensize(3)
    c4.begin_fill()
    for i in range(2):
        c4.circle(50)
        c4.penup()
        c4.fd(100)
        c4.pendown()
        c4.circle(50)
        for j in range(2):
            c4.right(90)
    c4.end_fill()
drawCircle4()

def drawSq():
    sq.setpos(0, 50)
    sq.pensize(3)
    for z in range(4):
        sq.fd(100)
        sq.right(90)
        sq.write(z)
drawSq()

window.exitonclick()
