from flask import Flask, request, jsonify, send_file, render_template
import os
from gtts import gTTS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tts', methods=['POST'])
def tts():
    data = request.get_json()
    text = data.get('text', '')

    # Verifying text is not empty
    if not text.strip():
        return jsonify({"error": "No text provided or text is empty"}), 400

    # Convertings text to speech
    tts = gTTS(text)
    filename = 'speech1.mp3'
    tts.save(filename)

    # Send the audio file as a response
    return send_file(filename, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
