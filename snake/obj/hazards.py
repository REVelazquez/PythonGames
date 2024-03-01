import turtle
import random

def create_hazard():
    hazard=turtle.Turtle()
    hazard.speed(0)
    hazard.shape('triangle')
    hazard.color('red')
    hazard.penup()
    x_hazard = random.randint(-280, 280)
    y_hazard = random.randint(-280, 280)
    hazard.shapesize(stretch_wid=0.75, stretch_len=0.75)
    hazard.goto(x_hazard, y_hazard)
    hazard.direction = 'stop'
    return hazard