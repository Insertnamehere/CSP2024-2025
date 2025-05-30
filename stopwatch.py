import tkinter as tk
from PIL import Image, ImageTk

wn = tk.Tk()
wn.title("Stopwatch")
wn.geometry("1600x1200")

secondsBase, minutesBase, hoursBase = 0, 0, 0

stopCondition = False
resetShow = False


configTime = tk.StringVar(wn)

configSecs = tk.StringVar(wn)
configMins = tk.StringVar(wn)
configHours = tk.StringVar(wn)

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

def update(stopCondition, resetCondition, seconds, minutes, hours):
    if(stopCondition == False):
        if(seconds >= 59):
            minutes += 1
            seconds = 0
        elif(minutes >= 59):
            hours += 1
            minutes = 0
            seconds = 0
        else:
            seconds += 1
            
        configSecs.set(value=str(f"{seconds:02d}"))

        configMins.set(value=str(f"{minutes:02d}"))

        configHours.set(value=str(f"{hours:02d}"))

        configTime = tk.StringVar()
        configTime.set(f"{configHours.get()} {":"} {configMins.get()} {":"} {configSecs.get()}")
        timeLabel.after(1000, lambda:(update(stop(), seconds, minutes, hours)))

        timeLabel.config(text= configTime.get())
        print(configTime.get())

    if(stopCondition == True):
        configTime = tk.StringVar()
        configTime.set(f"{configHours.get()} {configMins.get()} {configSecs.get()}")
        timeLabel.after(1000, lambda:(update(stop(), seconds, minutes, hours)))

        timeLabel.config(text= configTime.get())
        print(configTime.get())

    if(resetCondition == True):
        timeLabel.config(text= ("00:00:00"))

    resetShow = True
    return resetShow

def reset(resetted):
    resetCondition = resetted
    return stop(True), resetCondition

def stop(stopped):
    stopCondition = stopped
    return stopCondition


startButton = tk.Button(wn, text="Start", width=30, height=3, font=("Arial",50,"bold"), command= lambda:(update(stop(False), reset(False), secondsBase, minutesBase, hoursBase), startHide(), resetEnable(), stopShow()))
startButton.pack()

stopButton = tk.Button(wn, text="Stop", width=30, height=3, font=("Arial",40,"bold"), command= lambda:(stop(True), startShow(), stopHide()))

resetButton = tk.Button(wn, text="reset", width=30, height=3, font=("Arial",30,"bold"), state= tk.DISABLED, command= lambda:(reset(True), resetDisable(), startShow(),stopHide()))
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
