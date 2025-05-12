import tkinter as tk
import time as tm
import math as mt
from PIL import Image, ImageTk

wn = tk.Tk()
wn.title("Stopwatch")
wn.geometry("800x600")

timeVar = 0
timePrint = 0

timerStart = False

imgPath = "/Users/andrewkowalski/Documents/APCPS/images.png"

try:
    img = Image.open(imgPath)
    pic = ImageTk.PhotoImage(img)
    imgLabel = tk.Label(wn, image=pic)
    imgLabel.pack()
except FileNotFoundError:
    print(f"Error: Image file not found at {imgPath}")
    error_label = tk.Label(wn, text=f"Image not found: {imgPath}")
    error_label.pack()
except Exception as e:
    print(f"An error occurred: {e}")

time = tk.Label(wn, text="00:00:00", font=("Arial", 100,"bold"))
time.pack()

def update(seconds, minutes, hours):
    seconds += 1
    time.config(text= (hours,":",minutes,":",seconds))
    time.after(1000, update(seconds, minutes, hours))

def timeLogic():
    seconds = timeVar
    minutes = mt.fmod(timeVar)
    if(time > 59):
        timePrint = time 

def start():
    seconds, minutes, hours = 0, 0, 0
    update(seconds, minutes, hours)

def stop():
    None

def reset():
    stop()



startButton = tk.Button(wn, text="Start", width=30, height=3, font=("Arial",50,"bold"), command= start())
startButton.pack()

stopButton = tk.Button(wn, text="Stop", width=30, height=3, command= stop())
startButton.pack()

#make reset button go grey if time is already zeroed.
resetButton = tk.Button(wn, text="reset", command= reset())
startButton.pack()

wn.mainloop()
