import speech_recognition as sr

from os import system

def recognize(audio_file):
    AUDIO_FILE = f"./audios/{audio_file}"

    system(fr"ffmpeg -i {AUDIO_FILE} ./audios/output.wav")

    r = sr.Recognizer()
    with sr.AudioFile("./audios/output.wav") as source:
        audio = r.record(source)

    try:
        print("Google Speech Recognition thinks you said " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    recognize("test.mp3")
