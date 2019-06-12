import speech_recognition as sr
import os
import time

from src.wit import recognize_wit

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
        text, entity, values = recognize_wit(audio, wit_access_token)
        print(time.time() - time1)
        return text, entity, values
    except Exception as e:
        print(e)
        return None, None, None
