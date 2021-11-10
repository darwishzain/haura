import speech_recognition as sr
import pyttsx3

global engine
engine = pyttsx3.init('sapi5')
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