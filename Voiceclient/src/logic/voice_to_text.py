import speech_recognition as sr
import time


# records from mic and returns what it understood
#
def voice_2_text():
    time1 = time.time()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak:")
        print(time.time() - time1)
        audio = r.listen(source)  # todo hier muss die snowball configuration hin
        print("Finished")
    return audio_to_wav(audio)


def audio_to_wav(audio_data):
    assert isinstance(audio_data, sr.AudioData), "Data must be audio data"

    wav_data = audio_data.get_wav_data(
        convert_rate=None if audio_data.sample_rate >= 8000 else 8000,  # audio samples must be at least 8 kHz
        convert_width=2  # audio samples should be 16-bit
    )

    return wav_data
