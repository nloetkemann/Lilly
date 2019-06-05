import speech_recognition as sr


def voice_2_text():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Speak:")       
        r.adjust_for_ambient_noise(source)                                                                            
        audio = r.listen(source)
        print("Finished!")
    try:
        print("google :" + r.recognize_google(audio))
        #print("ibm: " + r.recognize_ibm(audio))
        print("sphinx: " + r.recognize_sphinx(audio))
    except Exception as e:
        print(e)
