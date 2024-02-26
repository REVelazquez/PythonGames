import turtle

def create_head():
    # Head settings
    # Turtle obj
    head = turtle.Turtle()
    # Para que sea fijo
    head.speed(0)
    #forma
    head.shape('circle')
    #color
    head.color('black')
    # Centrado
    head.goto(0, 0)
    # Para no dejar rastro de la animación
    head.penup()
    # Para que el programa espere para una dirección
    head.direction= 'stop'
    return head