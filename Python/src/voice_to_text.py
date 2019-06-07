import speech_recognition as sr
import os
import requests
import json
import time

from src.wit import record_audio, read_audio

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'
# Wit.ai api access token
wit_access_token = os.environ['WIT_TOKEN']


# records from mic and returns what it understood
def voice_2_text():
    time1 = time.time()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        print("Finished")
    try:
        value = r.recognize_wit(audio, wit_access_token)
        time2 = time.time()
        print(time2 - time1)
        return value, None, None
    except Exception as e:
        time2 = time.time()
        print(time2 - time1)
        print(e)
        return None, None, None


# records by default 5 seconds, sends direct api request
def voice_2_text2(num_seconds=5):
    time1 = time.time()
    audiofile = 'sounds/temp.wav'
    # record audio of specified length in specified audio file
    record_audio(num_seconds, audiofile)

    # reading audio
    audio = read_audio(audiofile)
    os.remove(audiofile)

    # defining headers for HTTP request
    headers = {'authorization': 'Bearer ' + wit_access_token,
               'Content-Type': 'audio/wav'}

    # making an HTTP post request
    resp = requests.post(API_ENDPOINT, headers=headers,
                         data=audio)

    # converting response content to JSON format
    data = json.loads(resp.content)

    # get text from data
    text = data['_text']
    if 'entities' in data:
        entities = list(data['entities'].keys())
        if len(entities) > 0:
            entity = entities[0]
            values = []
            for value in data['entities'][entity]:
                values.append(value['value'])
            time2 = time.time()
            print(time2 - time1)

            return text, entity, values

    # return the text
    time2 = time.time()
    print(time2 - time1)
    return text, None, None
