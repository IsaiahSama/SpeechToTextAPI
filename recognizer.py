import speech_recognition as sr

from os import system, path, remove

def recognize(audio_file):
    AUDIO_FILE = f"./audios/{audio_file}"

    if path.exists("./audios/output.wav"):
        remove("./audios/output.wav")

    try:
        system(fr"ffmpeg -i {AUDIO_FILE} ./audios/output.wav")
    except Exception as e:
        print(e)
        return {"error": e, "text": ""}

    if audio_file != "test.mp3":
        remove(AUDIO_FILE)

    r = sr.Recognizer()
    try:
        with sr.AudioFile("./audios/output.wav") as source:
            r.adjust_for_ambient_noise(source, 1)
            audio = r.record(source)
    except FileNotFoundError as e:
        print(e)
        return {"error": "Audio file not found on server.", "text": ""}

    text = ""
    try:
        text =  r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return {"error": "Audio could not be understood. Try again", "text": ""}
    
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return {"error": e, "text": ""}
    return {"text": text, "error": None}

if __name__ == "__main__":
    recognize("test.mp3")
