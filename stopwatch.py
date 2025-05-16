import tkinter as tk
from PIL import Image, ImageTk

wn = tk.Tk()
wn.title("Stopwatch")
wn.geometry("1600x1200")

secondsBase, minutesBase, hoursBase = 0, 0, 0

stopCondition = True
resetShow = False

imgPath = "/Users/andrewkowalski/Documents/APCPS/images.png"

try:
    img = Image.open(imgPath)
    pic = ImageTk.PhotoImage(img)
    imgLabel = tk.Label(wn, image=pic)
except FileNotFoundError:
    print(f"Error: Image file not found at {imgPath}")
    error_label = tk.Label(wn, text=f"Image not found: {imgPath}")
    error_label.pack()
except Exception as e:
    print(f"An error occurred: {e}")

timeLabel = tk.Label(wn, text="00:00:00", font=("Arial", 100,"bold"))
timeLabel.pack()

def stop():
    stopCondition = True
    return stopCondition

def update(stopCondition, seconds, minutes, hours):
    stopCondition = False
    if(stopCondition == False):
        if(seconds > 59):
            minutes += 1
            seconds = 0
        elif(minutes > 59):
            hours += 1
            minutes = 0
            seconds = 0
        configSecs = tk.StringVar(value=str(seconds)+":")
        configMins = tk.StringVar(wn, str(minutes) + ":")
        configHours = tk.StringVar(wn, str(hours) +":")
        configTime = tk.StringVar(wn, value=configHours+ configMins+ configSecs)
        timeLabel.config(text= configTime)
        print(configTime)
        timeLabel.after(1000, lambda:(update(stop(), seconds, minutes, hours)))
        
    resetShow = True
    return resetShow

def reset(seconds, minutes, hours):
    seconds, minutes, hours = 0, 0, 0
    stopCondition = True
    return stopc, seconds, minutes, hours


startButton = tk.Button(wn, text="Start", width=30, height=3, font=("Arial",50,"bold"), command= lambda:(update(stop(), secondsBase, minutesBase, hoursBase), startHide(), resetEnable(), stopShow()))
startButton.pack()

stopButton = tk.Button(wn, text="Stop", width=30, height=3, font=("Arial",40,"bold"), command= lambda:(stop(), startShow(), stopHide()))

resetButton = tk.Button(wn, text="reset", width=30, height=3, font=("Arial",30,"bold"), state= tk.DISABLED, command= lambda:(reset(secondsBase, minutesBase, hoursBase), resetDisable(), startShow(),stopHide()))
resetButton.pack()

imgLabel.pack()

def startHide():
    startButton.pack_forget()
def startShow():
    startButton.pack_configure(after= timeLabel)
def stopShow():
    stopButton.pack()
    stopButton.pack_configure(after= timeLabel)
def stopHide():
    stopButton.pack_forget()
def resetDisable():
    resetButton.config(state= tk.DISABLED)
def resetEnable():
    resetButton.config(state= tk.NORMAL)
wn.mainloop()
