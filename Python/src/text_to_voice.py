import os
from gtts import gTTS
import pyttsx3
from playsound import playsound
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[6].id)
print(voices)




# uses googles tts creates a mp3 and deletes it
def text_2_voice(text, remove=True):
    time1 = time.time()
    file = 'sounds/temp.mp3'
    tts = gTTS(text=text, lang='de')
    tts.save(file)
    playsound(file)
    if remove:
        os.remove(file)
    time2 = time.time()
    print(time2 - time1)


# doesnt create a file
def text_2_voice2(text):
    time1 = time.time()
    engine.say(text)
    engine.runAndWait()
    time2 = time.time()
    print(time2 - time1)
