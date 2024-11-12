# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----countdown variables-----
fontSetup = ("Arial", 20, "normal")
timer = 30
counterInterval = 1000   #1000 represents 1 second
timerUp = False

#-----game configuration----
spotColor = "pink"
spotSize = 2
spotShape = "circle"

score = 0
fontSetup = ("Arial", 75, "normal")
#-----initialize turtle-----
spot = trtl.Turtle()
spot.fillcolor(spotColor)
spot.shapesize(spotSize)
spot.shape(spotShape)

scoreWriter = trtl.Turtle()
scoreWriter.penup()
scoreWriter.hideturtle()
scoreWriter.goto(-325, 225)

counter =  trtl.Turtle()
#-----game functions--------
def spotClicked(x, y):
    changPosition()
    updateScore()

def changPosition():
    newXPos = rand.randint(-400, 400)
    newYPos = rand.randint(-300, 300)
    spot.goto(newXPos,newYPos)

def updateScore():
    scoreWriter.clear()
    global score
    score += 1
    scoreWriter.write(score, font = fontSetup)

def countdown():
    global timer, timer_up
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=fontSetup)
        timer_up = True
    else:
        counter.write("Timer: " + str(timer), font=fontSetup)
        timer -= 1
        print(timer)
    counter.getscreen().ontimer(countdown, counterInterval) 

#-----events----------------
spot.onclick(spotClicked)
wn = trtl.Screen()
wn.mainloop()
wn.ontimer(countdown, counterInterval)
