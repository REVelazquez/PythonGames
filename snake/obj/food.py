import turtle
import random

def create_food():
    food= turtle.Turtle()
    food.speed(0)
    food.shape('circle')
    food.color('red')
    food.penup()
    food.goto(0,0 )
    food.direction = 'stop'
    return food

def move_food(food):
    x_food = random.randint(-280, 280)
    y_food = random.randint(-280, 280)
    food.goto(x_food, y_food)