from src.logic.text_to_voice import text_2_voice
from src.logic.voice_to_text import voice_2_text
from src.wit.wit_response import WitResponse
from src.logic.handler import MessageHandler

if __name__ == "__main__":
    wit_response = voice_2_text()
    assert isinstance(wit_response, WitResponse)
    print(wit_response.get_keywords())
    handler = MessageHandler(wit_response)
    response = handler.handle_message()

    text_2_voice(response.text)
