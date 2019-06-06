import speech_recognition as sr
import os


def voice_2_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        audio = r.listen(source)
        print("Finished!")
    try:
        return r.recognize_wit(audio, os.environ['WIT_TOKEN'])
    except Exception as e:
        print(e)
        return None

def voice_2_text2():
	def send():
		pass
	
	
