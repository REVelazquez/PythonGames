import turtle
import random

def create_food():
    food= turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.penup()
    food.goto(0, 0)
    food.shapesize(stretch_wid=0.5, stretch_len=0.5)
    food.color('black')
    food.direction = 'stop'
    food.value = 0
    return food

def move_food(food):
    aleatorio=random.randint(1, 3)
    x_food = random.randint(-280, 280)
    y_food = random.randint(-280, 280)
    food.goto(x_food, y_food)
    if aleatorio==1:
        food.color('black')
        food.value=10
    elif aleatorio == 2:
        food.color('yellow')
        food.value=25
    elif aleatorio == 3:
        food.color('orange')
        food.value=50