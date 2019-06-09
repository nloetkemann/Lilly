import json
from urllib.request import Request, urlopen
from speech_recognition import AudioData, RequestError, UnknownValueError
from urllib.error import URLError, HTTPError


def recognize_wit(audio_data, key, show_all=False):
    assert isinstance(audio_data, AudioData), "Data must be audio data"
    assert isinstance(key, str), "``key`` must be a string"

    wav_data = audio_data.get_wav_data(
        convert_rate=None if audio_data.sample_rate >= 8000 else 8000,  # audio samples must be at least 8 kHz
        convert_width=2  # audio samples should be 16-bit
    )
    url = "https://api.wit.ai/speech?v=20160526"
    request = Request(url, data=wav_data,
                      headers={"Authorization": "Bearer {}".format(key), "Content-Type": "audio/wav"})
    try:
        response = urlopen(request, timeout=None)
    except HTTPError as e:
        raise RequestError("recognition request failed: {}".format(e.reason))
    except URLError as e:
        raise RequestError("recognition connection failed: {}".format(e.reason))
    response_text = response.read().decode("utf-8")
    result = json.loads(response_text)

    # return results
    if show_all: return result
    if "_text" not in result or result["_text"] is None: raise UnknownValueError()
    return result["_text"]
