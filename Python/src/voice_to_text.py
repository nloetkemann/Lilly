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
        print(e)
    try:
        return r.recognize_google(audio)
    except Exception as e:
        print(e)
    try:
        return r.recognize_ibm(audio)
    except Exception as e:
        print(e)
    try:
        return r.recognize_sphinx(audio)
    except Exception as e:
        print(e)
    try:
        return r.recognize_wit(audio)
    except Exception as e:
        print(e)
    try:
        return r.recognize_houndify(audio)
    except Exception as e:
        print(e)
