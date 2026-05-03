import pgzrun
from random import randint

WIDTH = 800
HEIGHT = 600
GRAVITY_STRENGTH = 1

egg = Actor('egg')
egg.pos = 400, 300

bird = Actor('bird-up')
bird.pos = randint(800, 1600), randint(10, 200)

house = Actor('house')
house.pos = randint(800, 1600), 460

tree = Actor('tree')
tree.pos = randint(800, 1600), 450

bird_up = True
up = False
game_over = False
score = 0
number_of_updates = 0
scores = []

def update_high_scores():
    global score, scores
    # Simplified filename to work in your current folder
    filename = 'high-scores.txt'
    try:
        with open(filename, 'r') as file:
            line = file.readline()
            high_scores = line.split()
    except:
        high_scores = ['0', '0', '0', '0', '0']

    scores = []
    for hs in high_scores:
        if score > int(hs):
            scores.append(str(score))
            score = int(hs)
        else:
            scores.append(str(hs))

    with open(filename, 'w') as file:
        file.write(" ".join(scores))

def display_high_scores():
    screen.draw.text('HIGH SCORES', (350, 150), color='black', fontsize=40)
    y = 200
    for i, hs in enumerate(scores):
        screen.draw.text(f"{i+1}. {hs}", (375, y), color='black', fontsize=30)
        y += 30

def draw():
    screen.blit('background', (0,0))
    if not game_over:
        egg.draw()
        bird.draw()
        house.draw()
        tree.draw()
        screen.draw.text('Score: ' + str(score), (700, 5), color='black')
    else:
        display_high_scores()

def on_mouse_down():
    global up
    up = True

def on_mouse_up():
    global up
    up = False

def flap():
    global bird_up
    bird.image = 'bird-down' if bird_up else 'bird-up'
    bird_up = not bird_up

def update():
    global game_over, score, number_of_updates
    if not game_over:
        # Movement logic
        if up:
            egg.y -= 2 # Smooth rising
        else:
            egg.y += GRAVITY_STRENGTH 

        if bird.x > -100:
            bird.x -= 4
            if number_of_updates == 9:
                flap()
                number_of_updates = 0
            else:
                number_of_updates += 1
        else:
            bird.x = randint(800, 1600)
            bird.y = randint(10, 200)
            score += 1

        if house.x > -100:
            house.x -= 2
        else:
            house.x = randint(800, 1600)
            score += 1

        if tree.x > -100:
            tree.x -= 2
        else:
            tree.x = randint(800, 1600)
            score += 1

        if egg.top < 0 or egg.bottom > 560 or \
           egg.colliderect(bird) or \
           egg.colliderect(house) or \
           egg.colliderect(tree):
            game_over = True
            update_high_scores()

pgzrun.go()