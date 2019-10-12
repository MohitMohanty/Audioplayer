import speech_recognition as sr
import os
from playsound import playsound
r = sr.Recognizer()

with sr.Microphone() as source:
    print("speak anything :  ")
    audio = r.listen(source)
try:
    text = r.recognize_google(audio)
    track = text.split(" ")
    ext='.mp3'
    text = track[1]+ext
    print("playing :{}".format(text))
    os.system("start "+text)
except:
    print("can't listen")

