from src.text_to_voice import text_2_voice, text_2_voice2
from src.voice_to_text import voice_2_text
import time

if __name__ == "__main__":
    text = voice_2_text()
    print(text)
    if text is not None and text != '':
        text_2_voice(text)
