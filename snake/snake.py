import turtle
import time
import random
from obj import create_food, move_food, create_head, create_text, create_hazard, mov, setup_keyboard_controls

delay = 0.1
body_segments=[]
score= 0
high_score = 0
max_distance = 280
min_distance = -280
variation = 10
off_screen = 1000
food = create_food()
head=create_head()
hazard=create_hazard()
text=create_text(score, high_score)
# Configuración de la pantalla
wn = turtle.Screen()
# Titulo
wn.title('Juego Snake')
# windos size
wn.setup(width=700, height=700)
# Background Color
wn.bgcolor('blue')

setup_keyboard_controls(head, wn, variation)

        
while True:
    wn.update()
    # Colisiones con la ventana

    if head.xcor() > max_distance or head.xcor() < min_distance or head.ycor() >max_distance or head.ycor() < min_distance or head.distance(hazard.position()) < 15:
        time.sleep(1)
        head.goto(0, 0)
        head.direction= 'stop'
        # Esconder segmentos:
        move_food(food)

        

        for segment in body_segments:
            segment.goto (1000, 1000)
        body_segments.clear()
        score = 0
        text.clear()
        text = create_text(score, high_score)


    # Colisiones de cabeza y comida
    if head.distance(food.position()) < 20:
        move_food(food)
        step=5
        x_food_position= food.xcor()
        y_food_position= food.ycor()
        x_hazard=0
        y_hazard=0
        while x_hazard==0:
            x_hazard= random.randrange(x_food_position-30, x_food_position+30, step)
        while y_hazard==0:
            y_hazard= random.randrange(y_food_position-30, y_food_position+30, step)

        hazard.goto(x_hazard, y_hazard)
            # Config de segmentos
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('circle')
        new_segment.color('gray')
        new_segment.penup()
        body_segments.append(new_segment)

        score += variation
        
        if score > high_score:
            high_score= score
        text.clear()
        text.write(f'Score {score}            High Score:{high_score}', align='center', font=('Arial', 24))

    # Colisiones con el cuerpo
    totalSeg = len(body_segments)
    
    for i in range(totalSeg - 1, 0, -1):
        x=body_segments[i-1].xcor()
        y=body_segments[i-1].ycor()
        body_segments[i].goto(x, y)
    if totalSeg > 0:
        x=head.xcor()
        y=head.ycor()
        body_segments[0].goto(x,y)
    mov(head, variation)
    for segment in body_segments:
        if segment.distance(head) < variation:
            time.sleep(1)
            head.goto(0, 0)
            head.direction= 'stop'
            #esconder segmentos
            for segment in body_segments:
                segment.goto (1000, 1000)
            body_segments.clear()

            score= 0
            text.clear()
            text = create_text(score, high_score)

    time.sleep(delay)

turtle.done()
