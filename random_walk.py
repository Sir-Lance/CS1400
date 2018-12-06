#Lance Peters
#CS1400
#MrAbrahasmTeng
#Project5
import turtle
import random
import math
import sys
from termcolor import colored
#GRADER -pip install termcolor
window = turtle.Screen()
windowTitle = "Project 5"

line = turtle.Turtle()
line.speed(0)
line.color("red")
#exception handler invalid input
while True:
    try:
        steps = int(input("How many steps are we taking boss?: "))
    except ValueError:
        print(colored("ERROR: Input needs to be a number", "red"))
        continue
    if steps <= 0:
        print(colored("ERROR: Value is negative or 0", "red"))
        continue
    else:
        break

print(colored("Executing...", "green"))
x = random.random()
y = random.random()
for z in range(steps):
    angle = (random.random() * 2 * math.pi)
    line.write(z)
    for i in range(steps):
        x = x + math.cos(angle)
        y = y + math.sin(angle)
        line.setpos(x, y)

line.color("black")
linex = line.xcor()
liney = line.ycor()
line.home()
dist = line.distance(linex, liney)
line.write(f"Distance:{dist:,.2f}")
print(colored("Complete. Click to Exit...", "green"))

window.exitonclick()
