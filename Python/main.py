from src.logic.text_to_voice import text_2_voice
from src.logic.voice_to_text import voice_2_text
from src.wit.wit_response import WitResponse
from src.logic.handler import MessageHandler

if __name__ == "__main__":
    wit_response = voice_2_text()
    assert isinstance(wit_response, WitResponse)
    handler = MessageHandler(wit_response)
    response = handler.handle_message()
    if response is not None:
        text_2_voice(response)
    else:
        text_2_voice(Response('ich konnte nicht verstehen was du mir gesagt hast'))
