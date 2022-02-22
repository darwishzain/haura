#import os
#import datetime
import pyttsx3

engine = pyttsx3.init()
engine.say("I will speak this text")
engine.runAndWait()







#def tts(text):
#      return os.system("espeak  -s 155 -a 200 "+text+" " )

#m = datetime.datetime.now().strftime("%I %M %S")
#tts("'Sir the time is"+str(int(m[0:2]))+" "+str(int(m[3:5]))+" : ' ")
#tts("morning"+"sir")
