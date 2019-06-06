import speech_recognition as sr


def voice_2_text():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")                                                                                   
        audio = r.listen(source)
        print("Finished!")
    try:
        return r.recognize_bing(audio)
    except Exception as e:
        return e
