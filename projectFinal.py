import turtle as trtl
import matplotlib as mpl

trtl.register_shape("Tstub", ((0,0),(0,10),(10,10),(10,20),(20,20),(20,10),(20,10),(30,10),(30,0)))
trtl.register_shape("Lstand", ((0,0),(0,10),(20,10),(20,-20),(10,-20),(10,0),(0,0)))
trtl.register_shape("Llong", ((0,0),(0,10),(30,10),(30,-20),(20,-20),(20,0)))

turtleTest = trtl.Turtle()
turtleTest.shape("Lstand")
turtleTest.shapesize(5)

Tstub = trtl.Turtle()
Tstub.shape("Tstub")

Lstand = trtl.Turtle()
Lstand.shape("Lstand")

wn = trtl.Screen()
wn.mainloop()
