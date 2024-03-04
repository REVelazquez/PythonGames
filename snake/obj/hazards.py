import turtle

def create_hazard():
    hazard=turtle.Turtle()
    hazard.speed(0)
    hazard.shape('triangle')
    hazard.color('red')
    hazard.penup()
    hazard.shapesize(stretch_wid=0.75, stretch_len=0.75)
    hazard.goto(1000, 1000)
    hazard.direction = 'stop'
    return hazard

