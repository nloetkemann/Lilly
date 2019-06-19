from src.logic.text_to_voice import text_2_voice
from src.logic.voice_to_text import voice_2_text

if __name__ == "__main__":
    text, entities, values = voice_2_text()
    text_2_voice(text)
