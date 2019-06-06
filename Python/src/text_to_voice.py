import os
from gtts import gTTS
import pyttsx3
from playsound import playsound

engine = pyttsx3.init()
engine.setProperty('rate', 150)


def text_2_voice(text, remove=False):
    file = 'sounds/temp.mp3'
    tts = gTTS(text=text, lang='de')
    tts.save(file)
    playsound(file)
    if remove:
        os.remove(file)


def text_2_voice2(text):
    engine.say(text)
    engine.runAndWait()
