import speech_recognition as sr
#! no module named speech_recognition
import pyttsx3
#! No module named pyttsx3

global engine
engine = pyttsx3.init('')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)

for voice in voices:
    print(voice.name)
    engine.setProperty('voices', voice.id)
    engine.say("Hello")
    engine.runAndWait()
    engine.stop()

##def voiceTalk(sentence):
##    engine.say(sentence)
##    engine.runAndWait()

##voiceTalk("Hello")