from src.grpc.client import Client
from src.logic.voice_to_text import voice_2_text

client = Client()

if __name__ == "__main__":
    audio_data = voice_2_text()
    file = open('./temp/temp.wav', 'wb')
    file.write(audio_data)
    client.upload_file(audio_data)
    # assert isinstance(wit_response, WitResponse)
    # handler = MessageHandler(wit_response)
    # response = handler.handle_message()
    # if response is not None:
    #     text_2_voice(response)
    # else:
    #     text_2_voice(Response('ich konnte nicht verstehen was du mir gesagt hast'))
