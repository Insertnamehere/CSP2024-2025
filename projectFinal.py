import turtle as trtl
import matplotlib as mpl

trtl.register_shape("Tstub", ((0,0),(0,10),(10,10),(10,20),(20,20),(20,10),(20,10),(30,10),(30,0)))
trtl.register_shape("Lstand", ((0,0),(0,10),(20,10),(20,-20),(10,-20),(10,0),(0,0)))
trtl.register_shape("Llong", ((0,0),(0,10),(30,10),(30,-20),(20,-20),(20,0)))

#Variables
#bool Checks
gameStart = True


wn = trtl.Screen()

turtleTest = trtl.Turtle()
turtleTest.shape("Tstub")


Tstub = trtl.Turtle()
Tstub.shape("Tstub")
Tstub.hideturtle()

Lstand = trtl.Turtle()
Lstand.shape("Lstand")
Lstand.hideturtle()

grid = trtl.Turtle()
grid.hideturtle()
grid.penup()
for i in 8:
    x = scaleX * i
    grid.goto(x, wn.window_height())
    grid.pendown()
    grid.down(wn.window_height())

def scales():
    global scaleX, scaleY
    print(wn.canvwidth, wn.canvheight)
    scaleX = wn.window_width() / int(8)
    scaleY = wn.window_height() / int(8)
    print(scaleX, scaleY)
    
    turtleTest.shapesize(scaleY/10, scaleX/10) 
scales()
wn.mainloop()
