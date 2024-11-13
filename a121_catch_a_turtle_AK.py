# a121_catch_a_turtle.py
#README. Go to fullscreen before starting. Timer gets cut off otherwise.
#-----import statements-----
import turtle as trtl
import random as rand

#-----countdown variables-----
fontSetup = ("Arial", 20, "normal")
timer = 30
counterInterval = 1000   #1000 represents 1 second
timerUp = False

#-----game configuration----
spotColors = ["pink", "red", "green", "orange", "blue", "yellow"]
spotShape = "circle"
spotSizes = [.5, .75, 1, 2, 3, 4, 5]


score = 0
fontSetup = ("Arial", 75, "normal")

#-----initialize turtle-----
spot = trtl.Turtle()
spot.fillcolor("pink")
spot.shapesize(2)
spot.shape(spotShape)
spot.penup()

scoreWriter = trtl.Turtle()
scoreWriter.penup()
scoreWriter.hideturtle()
scoreWriter.goto(-325, 225)

counter =  trtl.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(325, 225)
#-----game functions--------
def spotClicked(x, y):
    if(timer == 30):
        countdown()
    if(timerUp == False):
        changPosition()
        updateScore()
    else:
        spot.hideturtle()

def changPosition():
    spot.turtlesize(rand.choice(spotSizes))
    spot.fillcolor(rand.choice(spotColors))

    newXPos = rand.randint(-400, 400)
    newYPos = rand.randint(-300, 300)
    spot.goto(newXPos,newYPos)

def updateScore():
    scoreWriter.clear()
    global score
    score += 1
    scoreWriter.write(score, font = fontSetup)

def countdown():
    global timer, timerUp
    counter.clear()
    if timer <= 0:
        counter.write("Time's Up", font=fontSetup)
        timerUp = True
    else:
        counter.write("Timer: " + str(timer), font=fontSetup)
        timer -= 1
        print(timer)
    counter.getscreen().ontimer(countdown, counterInterval) 

#-----events----------------
spot.onclick(spotClicked)
wn = trtl.Screen()
wn.bgcolor("Light Blue")
wn.mainloop()
wn.ontimer(countdown, counterInterval)
