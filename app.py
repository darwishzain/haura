#tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pynput import keyboard
import speech_recognition #gui
from win32api import GetSystemMetrics #for now gettting resolution
from speech_recognition import *
import time
import pyttsx3
import psutil


window = tk.Tk()   
window.title("Haura System")
screenWidth = str(GetSystemMetrics(0))#get screen resolution(width) -> into string
screenHeight = str(GetSystemMetrics(1))#get screen resolution(height) -> into string
#because geometry don't accept integer
window.geometry(screenWidth+"x"+screenHeight)#widthxheight format
window.iconbitmap('./icon.ico')
tabControl = ttk.Notebook(window)

global engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def voiceTalk(sentence):
    engine.say(sentence)
    engine.runAndWait()


tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Home')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Settings')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Misc')
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='About')

tabControl.pack(expand=1, fill="both")

clockDisplay = Label(tab1, text="HH:MM::SS")
clockDisplay.grid(row=0, column=0)
dateDisplay = Label(tab1,text="DD")
dateDisplay.grid(row=1, column=0)
batteryDisplay = Label(tab1, text="#%")
batteryDisplay.grid(row=0, column=4) 

def update():
    global hour24, hour12, minute, second, day, month, year
    hour24 = time.strftime("%H")
    hour12 = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day  = time.strftime("%d")
    month  = time.strftime("%m")
    year  = time.strftime("%Y")
    clock = hour24 +":"+ minute +":"+ second
    clockDisplay.config(text=clock)
    date = day+"/"+month+"/"+year
    dateDisplay.config(text=date)
   

    global battery, plugged, percent
    battery = psutil.sensors_battery()
    percent = battery.percent
    plugged = battery.power_plugged
    batteryDisplay.config(text="battery : "+str(percent)+" %")
    if plugged==TRUE:
        voiceTalk("Plugged in")

    window.after(1000,update)

#telltime = Button(tab1, text="What time is it?", command=lambda:voiceTalk(hour24+minute+second+year))
#telltime.grid(row=2, column=0)
update()
voiceTalk("Hello there")
voiceTalk("The time is"+hour12+" hour"+minute+" minute"+second+"seconds")
window.mainloop()