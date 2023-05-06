import speech_recognition as sr

from os import system, path, remove

def recognize(audio_file):
    AUDIO_FILE = f"./audios/{audio_file}"

    if path.exists("./audios/output.wav"):
        remove("./audios/output.wav")

    system(fr"ffmpeg -i {AUDIO_FILE} ./audios/output.wav")

    remove(AUDIO_FILE)

    r = sr.Recognizer()
    with sr.AudioFile("./audios/output.wav") as source:
        audio = r.record(source)

    text = ""
    try:
       text =  r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return {"error": "Audio could not be understood. Try again"}
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return {"error": e}
    return {"text": text}

if __name__ == "__main__":
    recognize("test.mp3")
