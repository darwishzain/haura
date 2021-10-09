import function.voice as voice
#import function.about as about
#tkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pynput import keyboard
#import speech_recognition #gui
from win32api import GetSystemMetrics #for now gettting resolution
#from speech_recognition import *
import time
import psutil


window = tk.Tk()   
window.title("Haura System")
screenWidth = str(GetSystemMetrics(0))#get screen resolution(width) -> into string
screenHeight = str(GetSystemMetrics(1))#get screen resolution(height) -> into string
#because geometry don't accept integer
window.geometry(screenWidth+"x"+screenHeight)#widthxheight format
window.iconbitmap('./icon.ico')
tabControl = ttk.Notebook(window)



tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Home')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Settings')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Misc')
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='About')

tabControl.pack(expand=1, fill="both")

clockDisplay = Label(tab1, text="HH:MM::SS", font=("Arial",50))
clockDisplay.grid(row=0, column=0)
dateDisplay = Label(tab1,text="DD", font=("Arial",40))
dateDisplay.grid(row=1, column=0)
batteryDisplay = Label(tab1, text="#%", font=("Arial",30))
batteryDisplay.grid(row=0, column=5)
volumeScale = Scale(tab1,from_=0, to=100, fg="blue", orient=HORIZONTAL)
volumeScale.grid(row=3,column=7) 

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
    batteryDisplay.config(text=str(percent)+" %")
    
    if(percent>=70):
        batteryDisplay.config(fg="#00FF00")
    elif(percent>=50):
        batteryDisplay.config(fg="#FFFF00")
    elif(percent>=30):  
        batteryDisplay.config(fg="#FF0000")

    window.after(1000,update)#update time each second

#telltime = Button(tab1, text="What time is it?", command=lambda:voiceTalk(hour24+minute+second+year))
#telltime.grid(row=2, column=0)
v=0
def voiceChange():
    v+1
    voice.engine.setProperty('voices', voice.voices[v].id)
    voice.voiceTalk("Testing")
    print(voice.voices[v].name)


changeVoice = Button(tab1, text="Change", command=lambda:voiceChange())
changeVoice.grid(row=4,column=4)
update()
voice.voiceTalk("Welcome back")
window.mainloop()