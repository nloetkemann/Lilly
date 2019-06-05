import speech_recognition as sr


def voice_2_text():
    r = sr.Recognizer()
    harvard = sr.AudioFile('sounds/harvard.wav')
    with harvard as source:
        print('Say something')
        audio = r.record(source)
        print('Finished')

    try:
        print('Text' + r.recognize_google(audio))
    except:
        print('error')
