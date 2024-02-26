import turtle
import time
import random

delay = 0.1

body_segments=[]
score= 0
high_score = 0
# Configuración de la pantalla
wn = turtle.Screen()
# Titulo
wn.title('Juego Snake')
# windos size
wn.setup(width=700, height=700)
# Background Color
wn.bgcolor('blue')



# Head settings
# Turtle obj
head = turtle.Turtle()
# Para que sea fijo
head.speed(0)
#forma
head.shape('square')
#color
head.color('black')
# Centrado
head.goto(0, 0)
# Para no dejar rastro de la animación
head.penup()
# Para que el programa espere para una dirección
head.direction= 'stop'

# Food config:
food= turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
x_food = random.randint(-280, 280)
y_food = random.randint(-280, 280)
food.goto(x_food, y_food)
food. direction = 'stop'

#   Score
text=turtle.Turtle()
text.speed(0)
text.color('black')
text.penup()
text.hideturtle()
text.goto(0,300)
text.write(f'Score 0            High Score:0', align='center', font=('Arial', 24))

def mov():
    if head.direction == 'up':
        #almacenaremos el valor actual de la coord y
        y = head.ycor()
        head.sety(y + 10)
    if head.direction == 'down':
        #almacenaremos el valor actual de la coord y
        y = head.ycor()
        head.sety(y - 10)
    if head.direction == 'right':
        # almacenar el valor actual de la coord X
        x = head.xcor()
        head.setx(x + 10)
    if head.direction == 'left':
        # almacenar el valor actual de la coord X
        x = head.xcor()
        head.setx(x - 10)
def dirUp():
    head.direction= 'up'
def dirDown():
    head.direction= 'down'
def dirLeft():
    head.direction= 'left'
def dirRight():
    head.direction= 'right'
# conectar con teclado
wn.listen()
wn.onkeypress(dirUp, 'Up')
wn.onkeypress(dirDown, 'Down')
wn.onkeypress(dirLeft, 'Left')
wn.onkeypress(dirRight, 'Right')

        
while True:
    wn.update()
    # Colisiones con la ventana

    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() >280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0, 0)
        head.direction= 'stop'
        # Esconder segmentos:
        x_food = random.randint(-280, 280)
        y_food = random.randint(-280, 280)
        food.goto(x_food, y_food)

        for segment in body_segments:
            segment.goto(1000, 1000)
        body_segments.clear()
        score = 0
        text.clear()
        text.write(f'Score {score}            High Score:{high_score}', align='center', font=('Arial', 24))


    # Colisiones de cabeza y comida
    if head.distance(food)<  20:
        x=random.randint(-270, 270 )
        y=random.randint(-270, 270)
        food.goto(x, y)

        # Config de segmentos
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('gray')
        new_segment.penup()
        body_segments.append(new_segment)

        score+=10
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
    mov()
    for segment in body_segments:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0, 0)
            head.direction= 'stop'
            #esconder segmentos
            for segment in body_segments:
                segment.goto(1000, 1000)
            body_segments.clear()

            score= 0
            text.clear()
            text.write(f'Score {score}            High Score:{high_score}', align='center', font=('Arial', 24))

    time.sleep(delay)

turtle.done()
