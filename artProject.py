#INSTRUCTIONS
#Write Next or Back to switch between the Football Field, Soccer Field and Tennis Court.
#Watch the image change after you input 'Next' or 'Back'

import turtle as trtl
painter = trtl.Turtle()

i = 0
painter.speed(100)
fieldlist = ['Football', 'Soccer', 'Tennis', None]
w = 0
m = 0

print("Type 'Next' or 'Back' to find your favorite Sports field/Court.")

painter.hideturtle()

def drawFootball():
    painter.penup()
    painter.pensize(10)
    painter.goto(-350, 200)
    painter.pencolor("Black")
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor("Green")
    for i in range(2):
        painter.forward(600)
        painter.right(90)
        painter.forward(272)
        painter.right(90)
    painter.end_fill()
    painter.penup()
    painter.goto(-300, 200)
    painter.pencolor('White')
    painter.setheading(-90)
    painter.pensize(2)
    for i in range(21):
        painter.pendown()
        painter.forward(272)
        painter.penup()
        painter.sety(200)
        painter.setx(painter.xcor() + 25)
def drawSoccer():
    painter.seth(0)
    painter.penup()
    painter.pensize(5)
    painter.color('Black')
    painter.goto(-300, 225)
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor('Green')
    for i in range(2):
        painter.forward(600)
        painter.right(90)
        painter.forward(450)
        painter.right(90)
    painter.end_fill()
    painter.penup()
    painter.goto(0, -65)
    painter.pendown()
    painter.pencolor("White")
    painter.pensize(2)
    painter.circle(65)
    painter.goto(0, 225)
    painter.goto(0, -225)
    painter.penup()
    painter.goto(-300, 88)
    painter.pendown()
    for i in range(2):
        painter.forward(72)
        painter.right(90)
        painter.forward(176)
        painter.right(90)
    painter.penup()
    painter.goto(300, 88)
    painter.pendown()
    for i in range(2):
        painter.forward(-72)
        painter.left(90)
        painter.forward(-176)
        painter.left(90)
    painter.penup()
    painter.goto(300, 40)
    painter.pendown()
    for i in range(2):
        painter.forward(-24)
        painter.left(90)
        painter.forward(-80)
        painter.left(90)
    painter.penup()
    painter.goto(-300, 40)
    painter.pendown()
    for i in range(2):
        painter.forward(24)
        painter.right(90)
        painter.forward(80)
        painter.right(90)
    painter.penup()
    painter.turtlesize(.5)
    painter.color("White", "White")
    painter.shape("circle")
    painter.goto(-252, 0)
    painter.stamp()
    painter.goto(252, 0)
    painter.stamp()
    painter.goto(0, 0)
    painter.stamp()
    #painter.goto(-300, 225)
    #painter.stamp()
    #painter.goto(300, 225)
    #painter.stamp()
    #painter.goto(-300, -225)
    #painter.stamp()
    #painter.goto(300, -225)
    #painter.stamp() 
def drawTennis():
    painter.penup()
    painter.pensize(3)
    painter.color('Black')
    painter.goto(-300, 137.5)
    painter.pendown()
    painter.begin_fill()
    painter.fillcolor('Blue')
    for i in range(2):
        painter.forward(600)
        painter.right(90)
        painter.forward(275)
        painter.right(90)
    painter.end_fill()
    painter.penup()
    painter.pencolor("White")
    painter.sety(painter.ycor() - 35)
    painter.pendown()
    painter.forward(600)
    painter.penup()
    painter.goto(-300, -102.5)
    painter.pendown()
    painter.forward(600)
    painter.penup()
    painter.goto(-161.5, 0)
    painter.pendown()
    painter.forward(323)
    painter.penup()
    painter.goto(-161.5, 102.5)
    painter.setheading(-90)
    painter.pendown()
    painter.forward(205)
    painter.penup()
    painter.goto(161.5, 102.5)
    painter.pendown()
    painter.forward(205)
    painter.penup()
    painter.pencolor("Red")
    painter.goto(0, 150)
    painter.pendown()
    painter.forward(300)
    
while(0 == 0):

    if(m == 0):
        trtl.clearscreen()
        drawFootball()
    elif(m == 1):
        trtl.clearscreen()
        drawSoccer()
    elif(m == 2):
        trtl.clearscreen()
        drawTennis()
    
    change = input()
    if(change == 'Next'):
        w = fieldlist[m + 1]
        print(w)
        m = m + 1
    elif(change == 'Back'):
        w = fieldlist[m - 1]
        print(w)
        m = m - 1

    if(m == -1):
        print("Can't go further.")
        m = 0
    elif(m == 3):
        print("Can't go further.")
        m = 2
    

        
        
wn = trtl.Screen()
wn.mainloop()
