import turtle

def create_head():
    # Head settings
    # Turtle obj
    head = turtle.Turtle()
    head.speed(0)
    head.shape('circle')
    head.color('black')
    head.goto(0, 0)
    head.penup()
    head.direction= 'stop'
    return head