#Bryan Morris
#9/27/19
#GUI  Clock
import time
import calendar
from tkinter import *
from tkinter import ttk
from tkinter import font
import winsound

h = 0
m = 0
s = 0
t = "am"
def currentTime(h,m,s,t):
    totalSeconds = calendar.timegm(time.gmtime())
    currentSecond = totalSeconds % 60

    totalMinutes = totalSeconds // 60
    currentMinute = totalMinutes % 60

    totalHours = totalMinutes // 60
    currentHour = (totalHours % 24) - 6

    amPm = " "
    if currentHour>= 12:
        currentHour = currentHour - 12
        amPm = "PM"
        if currentHour == 0:
            currentHour=currentHour + 12
    else:
        amPm = "AM"
        if currentHour == 0:
            currentHour = currentHour + 12
    alarm = str(h) + ":" + str(m) + ":" + str(s) + t
    timex = str(currentHour) + ":" + str(currentMinute) + ":" + str(currentSecond) + " " + amPm

    if timex == alarm:
        beep()

    return timex
def beep():
    winsound.Beep(640,5000)
def showTime():
    global h
    global m
    global s
    global t
    time = currentTime(h,m,s,t)
    txt.set(time)
    root.after(1000, showTime)

def getAlarm(*args):
    global h
    h = input("what hour")
    global m
    m = input("what minute")
    global s
    s = input("what second")
    global t
    t = input("am or pm").upper()
def quit(*args):
    root.destroy()
#create root window
root = Tk()
root.geometry("500x200")
root.attributes("-fullscreen" ,False)
root.title("Alarm Clock")

#set window background color
root.configure(background = '#003366')
root.bind("x", quit)
root.bind("a", getAlarm)
root.after(1000, showTime)
#create font
fnt = font.Font(family="ComicSans", size = 60, weight = 'bold')
txt=StringVar()

#display time and set up the colors of text and background
lbl = ttk.Label(root, textvariable = txt, font = fnt, foreground = "green",background = 'yellow')
# place time in the center of the screen
lbl.place(relx=0.5, rely=0.5, anchor = CENTER)
# start main loop
root.mainloop()
