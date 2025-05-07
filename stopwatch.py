import tkinter  as tk
def changelabel():
    label1.config(text=myvariable.get())

window = tk.Tk()
window.title("my first window")

label1 = tk.Label(window, text="Hello GUI", bg="#00ff00")
label1.pack()

myvariable = tk.StringVar(value="change")
print(myvariable.get())

startButton = tk.Button(window, text="Press here", command= changelabel)
startButton.pack()

stopButton = tk.Button(window)


myCanvas = tk.Canvas(window, width=500, height=500)
myCanvas.pack()

rect= myCanvas.create_rectangle(10,10,100,100,fill="purple")
hexa= myCanvas.create_polygon(50, 250, 200, 50, 350, 250)

window.mainloop()
