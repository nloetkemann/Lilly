import os
from gtts import gTTS
import pyttsx3
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)


# uses googles tts creates a mp3 and deletes it
# takes 2 sec for a "Hello"
def text_2_voice(text, remove=True):
    time1 = time.time()
    file = 'sounds/temp.mp3'
    gTTS(text=text, lang='de').save(file)
    os.system("mpg123 " + file)
    if remove:
        os.remove(file)
    time2 = time.time()
    print(time2 - time1)


# doesnt create a file and faster
# takes 0.8 sec for a "Hello"
def text_2_voice2(text):
    time1 = time.time()
    engine.say(text)
    engine.runAndWait()
    time2 = time.time()
    print(time2 - time1)
