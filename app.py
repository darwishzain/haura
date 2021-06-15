#IMPORT
import pyttsx3
from pynput import keyboard
import psutil


'''the code'''
def voiceSetup():
    global engine 
    global sentence
    engine = pyttsx3.init() #object creation
    #set voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[3].id)
    print(voices[4].name)
    print(voices[1].name)
    print(voices[2].name)
    print(voices[3].name)
    #set rate
    rate = engine.getProperty('rate')
    print("rates:"+ str(rate))
    engine.setProperty('rate',125)

def voiceTalk(sentence):
    engine.say(sentence)
    engine.runAndWait()

def batteryInfo():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    print(percent+'% '+plugged)
    voiceTalk("battery is"+plugged+"and at"+percent+"percent")


voiceSetup()
voiceTalk("Hello. My name is howra")
#batteryInfo()
