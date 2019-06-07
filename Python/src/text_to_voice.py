import os
from gtts import gTTS
import pyttsx3
from playsound import playsound
import time
from pydub import AudioSegment
from pydub.playback import play

engine = pyttsx3.init()
engine.setProperty('rate', 150)


# uses googles tts creates a mp3 and deletes it
# takes 4,7 sec for a "Hello"
def text_2_voice(text, remove=True):
    time1 = time.time()
    file = 'sounds/temp.mp3'
    tts = gTTS(text=text, lang='de')
    print("nach gtts " + str(time.time() - time1))
    tts.save(file)
    print("nach save " + str(time.time() - time1))
    os.system("mpg123 " + file)
    print("nach play " + str(time.time() - time1))
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
