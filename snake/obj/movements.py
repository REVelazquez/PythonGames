
def mov(head, variation):
    if head.direction == 'up':
        #almacenaremos el valor actual de la coord y
        y = head.ycor()
        head.sety(y + variation)
    if head.direction == 'down':
        #almacenaremos el valor actual de la coord y
        y = head.ycor()
        head.sety(y - variation)
    if head.direction == 'right':
        # almacenar el valor actual de la coord X
        x = head.xcor()
        head.setx(x + variation)
    if head.direction == 'left':
        # almacenar el valor actual de la coord X
        x = head.xcor()
        head.setx(x - variation)


def setup_keyboard_controls(head, wn, variation):
    def dirUp():
        head.direction= 'up'
    def dirDown():
        head.direction= 'down'
    def dirLeft():
        head.direction= 'left'
    def dirRight():
        head.direction= 'right'
    wn.listen()
    wn.onkeypress(dirUp, 'Up')
    wn.onkeypress(dirDown, 'Down')
    wn.onkeypress(dirLeft, 'Left')
    wn.onkeypress(dirRight, 'Right')    