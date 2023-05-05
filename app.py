from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/transcribe/", methods=["POST"])
def transcribe():
    print("TRANSCRIBE ROUTE HIT!")