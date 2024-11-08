from flask import Flask, render_template, request, jsonify, Response
from json import dumps
from recognizer import recognize

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe", methods=["POST"])
def transcribe():
    audio_file = request.files.get("audio", None)
    if not audio_file:
        return Response(dumps({"error": "No audio file was received. Expected a file named 'audio'", "text": ""}), status=400, mimetype="application/json")

    audio_file.save(f"./audios/{audio_file.filename}")

    data = recognize(audio_file.filename)

    if data["error"] != None:
        return Response(dumps(data), status=400, mimetype="application/json")
        
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)