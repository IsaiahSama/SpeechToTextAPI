from flask import Flask, render_template, request, jsonify
from recognizer import recognize
from os import remove

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe/", methods=["POST"])
def transcribe():
    audio_file = request.files.get("audio", None)

    if not audio_file:
        return "FAILURE!"

    audio_file.save(f"./audios/{audio_file.filename}")

    data = recognize(audio_file.filename)

    remove(f"./audios/{audio_file.filename}")

    if "error" in data:
        return "AN ERROR OCCURED!"
    
    return jsonify(data)