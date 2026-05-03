import pgzrun

WIDTH = 1280
HEIGHT = 720

# Boxes
mainbox = Rect(50, 40, 820, 240)
timerbox = Rect(990, 40, 240, 240)
answerbox1 = Rect(50, 358, 495, 165)
answerbox2 = Rect(735, 358, 495, 165)
answerbox3 = Rect(50, 538, 495, 165)
answerbox4 = Rect(735, 538, 495, 165)
answerboxes = [answerbox1, answerbox2, answerbox3, answerbox4]

# Variables
score = 0
timeleft = 10

q1 = ["Who was the King Of The Pirates?", "Ace", "Roger", "Oden", "Whitebeard", 2]
q2 = ["Who rules The World Government?", "Imu", "Luffy", "Joyboy", "Wapol", 1]
q3 = ["Who killed Oden?", "Luffy", "Big Mom", "Zoro", "Kaido", 4]
q4 = ["Who is the navigator of The Straw Hats?", "Luffy", "Zoro", "Nami", "Whitebeard", 3]
q5 = ["Who is the worlds greatest swordsman?", "King", "Luffy", "Zoro", "Mihawk", 4]

questions = [q1, q2, q3, q4, q5]
question = questions.pop(0) 

def draw():
    screen.fill("dim grey")
    screen.draw.filled_rect(mainbox, "sky blue")
    screen.draw.filled_rect(timerbox, "sky blue")

    for box in answerboxes:
        screen.draw.filled_rect(box, "orange")

    screen.draw.textbox(str(timeleft), timerbox, color="black")
    screen.draw.textbox(question[0], mainbox, color="black")

    index = 1
    for box in answerboxes:
        screen.draw.textbox(question[index], box, color="black")
        index += 1

def gameover():
    global question, timeleft
    message = "Game Over. You got %s questions correct" % str(score)
    question = [message, "-", "-", "-", "-", 5]
    timeleft = 0

def correctanswer():
    global question, score, timeleft
    score += 1
    if questions:
        question = questions.pop(0)
        timeleft = 10
    else:
        gameover()

def on_mouse_down(pos):
    index = 1
    for box in answerboxes:
        if box.collidepoint(pos):
            if index == question[5]:
                correctanswer()
            else:
                gameover()
        index += 1

def update_time_left():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
    else: 
        gameover()

clock.schedule_interval(update_time_left, 1.0)

pgzrun.go()