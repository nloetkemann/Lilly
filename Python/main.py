from src.logic.text_to_voice import text_2_voice
from src.logic.voice_to_text import voice_2_text
from src.wit.wit_response import WitResponse

if __name__ == "__main__":
    response = voice_2_text()
    assert isinstance(response, WitResponse)
    text_2_voice(response.text)
