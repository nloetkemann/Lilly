import speech_recognition as sr
import os
import requests
import json
import time

from src.wit import record_audio, read_audio, recognize_wit

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'
# Wit.ai api access token
wit_access_token = os.environ['WIT_TOKEN']


# records from mic and returns what it understood
#
def voice_2_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        print("Finished")
    try:
        time1 = time.time()
        value = recognize_wit(audio, wit_access_token)
        print(time.time() - time1)
        return value, None, None
    except Exception as e:
        print(e)
        return None, None, None
