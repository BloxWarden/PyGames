import pgzrun
import random

FONTCOLOUR = (255, 255, 255)
WIDTH = 800
HEIGHT = 600
CENTREX = WIDTH / 2
CENTREY = HEIGHT / 2
CENTRE = (CENTREX, CENTREY)
FINALLEVEL = 8
STARTSPEED = 10
COLOURS = ["green", "blue"]

gameover = False
gamecomplete = False
currentlevel = 1
stars = []
animations = []

def draw():
    screen.clear()
    screen.blit("space", (0, 0))
    if gameover:
        display_message("Game Over!", "Try Again")
    elif gamecomplete:
        display_message("You Won!", "Well Done.")
    else:
        for star in stars:
            star.draw()

def update():
    global stars
    if not stars and not gameover and not gamecomplete:
        stars = make_stars(currentlevel)

def make_stars(number_of_extra_stars):
    colours_to_create = get_colours_to_create(number_of_extra_stars)
    new_stars = create_stars(colours_to_create) # Added this missing step
    layout_stars(new_stars)
    animate_stars(new_stars)
    return new_stars

def get_colours_to_create(number_of_extra_stars):
    colours_to_create = ["red"]
    for i in range(0, number_of_extra_stars):
        colours_to_create.append(random.choice(COLOURS))
    return colours_to_create

def create_stars(colours_to_create):
    new_stars = []
    for colour in colours_to_create:
        star = Actor(colour + "-star")
        new_stars.append(star)
    return new_stars

def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)
    for index, star in enumerate(stars_to_layout):
        star.x = (index + 1) * gap_size
        # Change this from 0 to the star's height so it starts just below the top edge
        star.y = star.height

def animate_stars(stars_to_animate):
    for star in stars_to_animate:
        duration = STARTSPEED - currentlevel
        star.anchor = ("center", "bottom")
        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)

def handle_game_over():
    global gameover
    gameover = True

def on_mouse_down(pos):
    global stars
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else: 
                handle_game_over()

def red_star_click():
    global currentlevel, stars, animations, gamecomplete
    stop_animations(animations)
    if currentlevel == FINALLEVEL:
        gamecomplete = True
    else:
        currentlevel += 1
        stars = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text): # Fixed typo in function name
    screen.draw.text(heading_text, fontsize=60, center=CENTRE, color=FONTCOLOUR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTREX, CENTREY + 30), color=FONTCOLOUR) 

pgzrun.go()