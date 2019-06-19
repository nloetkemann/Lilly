import os
from speech_recognition import AudioData, UnknownValueError
from wit import Wit

from src.wit.wit_response import WitResponse

wit_access_token = os.environ['WIT_TOKEN']
client = Wit(wit_access_token)


def __extract_infos(result, show_all):
    if show_all: return result
    if "_text" not in result or result["_text"] is None: raise UnknownValueError

    if len(result["entities"].keys()) > 0:
        list_entities = list(result["entities"].keys())
        entities = {}
        for entity in list_entities:
            values = []
            for value in result["entities"][entity]:
                values.append(value["value"])
                if 'unit' in value:
                    values.append(value['unit'])
            entities[entity] = values
        return WitResponse(result["_text"], entities)
    return WitResponse(result["_text"], None)


def recognize_wit(audio_data, show_all=False):
    assert isinstance(audio_data, AudioData), "Data must be audio data"
    assert isinstance(wit_access_token, str), "``key`` must be a string"

    wav_data = audio_data.get_wav_data(
        convert_rate=None if audio_data.sample_rate >= 8000 else 8000,  # audio samples must be at least 8 kHz
        convert_width=2  # audio samples should be 16-bit
    )

    result = client.speech(wav_data, None, {'Content-Type': 'audio/wav'})

    return __extract_infos(result, show_all)


def test():
    pass
