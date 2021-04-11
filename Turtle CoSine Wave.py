import math
import turtle

window = turtle.Screen()
window.bgcolor("black")
Ricardo = turtle.Turtle()
Ricardo.speed(10)
Turters = turtle.Turtle()
Turters.speed(10)
test = turtle.Turtle()

def makeAxis(turtle):
    test.color('white')
    test.goto(-360,0)
    test.forward(720)
    test.penup()
    test.goto(0,1.5)
    test.pendown()
    test.right(90)
    test.forward(3)
    test.penup()
    test.goto(0,2)


window = turtle.Screen()
window.reset()
window.setworldcoordinates(-360,-1.5,360,1.5)
makeAxis(test)

Ricardo.penup()
Turters.penup()

for angle in range(-360,360):
    Ricardo.color('blue')
    Ricardo.width(3)
    Ricardo.speed(10)
    
    y = math.sin(math.radians(angle))
    Ricardo.goto(angle,y)
    Ricardo.pendown()

for angle in range(-360,360):
    Turters.color('red')
    Turters.width(3)
    Turters.speed(10)
    
    y = math.cos(math.radians(angle))
    Turters.goto(angle,y)
    Turters.pendown()
