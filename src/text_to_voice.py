import os
from gtts import gTTS


def text_2_voice(text, remove=False):
    file = 'sounds/temp.wav'
    tts = gTTS(text=text, lang='de')
    tts.save(file)
    os.system("mpg123 " + file)
    if remove:
	    os.remove(file)
