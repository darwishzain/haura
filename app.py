#IMPORT
import pyttsx3
from pynput import keyboard
import psutil #for battery
from tkinter import *
import speech_recognition #gui
from win32api import GetSystemMetrics #for now gettting resolution
from speech_recognition import *
import time


'''Start Interface'''
window = Tk()
window.title("Haura")
screenWidth = str(GetSystemMetrics(0))#get screen resolution(width) -> into string
screenHeight = str(GetSystemMetrics(1))#get screen resolution(height) -> into string
#because geometry don't accept integer
window.geometry(screenWidth+"x"+screenHeight)#widthxheight format
window.configure(bg="white")



'''setup'''
def voiceSetup():
    global engine 
    global sentence
    engine = pyttsx3.init() #object creation
    #set voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    #set rate
    rate = engine.getProperty('rate')
    print("rates:"+ str(rate))
    engine.setProperty('rate',125)

def timeSetup():
    global hour, minute, second
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

def batterySetup():
    global battery, plugged, percent
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    plugged = "Plugged In" if plugged else "Not Plugged In"
    percent = str(battery.percent)

def speechIn():#dont know why yet
    global r
    r = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("Talk")
        audio_text = r.listen(source)
        print("Time over, thanks")
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
        try:
            # using google speech recognition
            print("Text: "+r.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")

def voiceTalk(sentence):
    engine.say(sentence)
    engine.runAndWait()

def batteryFull():
    voiceTalk("Battery is Full")

voiceSetup()
timeSetup()
batterySetup()
'''Interface Setup'''
Label(window, text='Battery :'+str(battery.percent)+'%').pack(side=LEFT)
clockTxt = Label(window, text=hour+":"+minute+":"+second).pack(side=LEFT)
batteryBtn = Button(window, text="Check Battery", command=lambda:voiceTalk("battery is"+plugged+"and at"+percent+"percent")).pack(side=LEFT)
hauraBtn = Button(window, text="Haura", command=lambda:voiceTalk('Hello')).pack(side=LEFT)
talkBtn = Button(window, text="Shaberu", command=speechIn).pack(side=LEFT)

#strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
window.mainloop()