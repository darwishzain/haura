import pyttsx3

#tts engine
global engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def voiceTalk(sentence):
    engine.say(sentence)
    engine.runAndWait()