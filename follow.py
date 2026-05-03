import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

dots = []
lines = []
nextdot = 0

def create_dots():
    global dots
    dots = []
    for dot in range(0, 10):
        actor = Actor("dot")
        actor.pos = randint(20, WIDTH - 20), randint(20, HEIGHT - 20)
        dots.append(actor)

create_dots()

def draw():
    screen.fill("black")
    number = 1
    for dot in dots:
        screen.draw.text(str(number), (dot.pos[0], dot.pos[1] + 12))
        dot.draw()
        number += 1
    for line in lines:
        screen.draw.line(line[0], line[1], (100, 0, 0))

def on_mouse_down(pos):
    global nextdot, lines
    
    if dots[nextdot].collidepoint(pos):
        if nextdot > 0:
            lines.append((dots[nextdot - 1].pos, dots[nextdot].pos))
        
        nextdot = nextdot + 1
        
        if nextdot == 10:
            nextdot = 0
            lines = []
            create_dots() 
    else:
        lines = []
        nextdot = 0

pgzrun.go()