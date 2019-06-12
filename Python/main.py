from src.text_to_voice import text_2_voice, text_2_voice2
from src.voice_to_text import voice_2_text

if __name__ == "__main__":
    text, _, _ = voice_2_text()
    text_2_voice(text)
