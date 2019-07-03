import speech_recognition as sr
import os
import time

from src.wit.wit import recognize_wit

# Wit speech API endpoint
API_ENDPOINT = 'https://api.wit.ai/speech'
# Wit.ai api access token
wit_access_token = os.environ['WIT_TOKEN']

def wait_for_hotword():
    pass


# records from mic and returns what it understood
#
def voice_2_text():
    time1 = time.time()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        print(time.time() - time1)
        audio = r.listen(source, snowboy_configuration=('./src/snowball/', ['./assets/Lilly.pmdl']))  # todo hier muss die snowball configuration hin
        print("Finished")
    try:
        response = recognize_wit(audio)
        return response
    except Exception as e:
        print(e)
        return None
