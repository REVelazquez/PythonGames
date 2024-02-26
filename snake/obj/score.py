import turtle

def create_text(score, high_score):
    #   Score
    text=turtle.Turtle()
    text.speed(0)
    text.color('black')
    text.penup()
    text.hideturtle()
    text.goto(0,300)
    text.write(f'Score {score}            High Score:{high_score}', align='center', font=('Arial', 24))

    return text