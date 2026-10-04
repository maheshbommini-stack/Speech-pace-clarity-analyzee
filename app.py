from flask import Flask, render_template, request, jsonify
import os
import tempfile
import wave
import contextlib
import math

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 25 * 1024 * 1024

ALLOWED_EXTENSIONS = {"wav"}


def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def analyze_wav(path):
    with contextlib.closing(wave.open(path, "rb")) as audio:

        channels = audio.getnchannels()
        sample_width = audio.getsampwidth()
        sample_rate = audio.getframerate()
        frames = audio.getnframes()

        duration = frames / float(sample_rate) if sample_rate else 0

        raw = audio.readframes(frames)

    # Analyze PCM samples
    if sample_width == 2:

        import array

        samples = array.array("h")
        samples.frombytes(raw)

        peak = max(
            (abs(x) for x in samples),
            default=0
        ) / 32768

        rms = math.sqrt(
            sum(x * x for x in samples) /
            max(len(samples), 1)
        ) / 32768

    elif sample_width == 1:

        values = list(raw)

        peak = max(
            (abs(x - 128) for x in values),
            default=0
        ) / 128

        rms = math.sqrt(
            sum((x - 128) ** 2 for x in values) /
            max(len(values), 1)
        ) / 128

    else:
        peak = 0
        rms = 0

    # Educational clarity estimate
    clarity = min(
        100,
        max(
            0,
            round(
                55 +
                (rms * 70) -
                (max(0, peak - 0.92) * 100)
            )
        )
    )

    if duration < 2:
        sample_type = "Very short sample"
    elif duration < 6:
        sample_type = "Short sample"
    elif duration < 20:
        sample_type = "Conversation length"
    else:
        sample_type = "Extended sample"

    if rms < 0.03:
        loudness = "Very quiet"
    elif rms < 0.10:
        loudness = "Moderate"
    elif rms < 0.25:
        loudness = "Strong"
    else:
        loudness = "Very strong"

    return {
        "duration": round(duration, 2),
        "sample_rate": sample_rate,
        "channels": channels,
        "peak": round(peak, 3),
        "rms": round(rms, 3),
        "clarity_score": clarity,
        "loudness": loudness,
        "sample_type": sample_type
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "audio" not in request.files:
        return jsonify({
            "error": "No audio file was selected."
        }), 400

    audio = request.files["audio"]

    if not audio.filename:
        return jsonify({
            "error": "Please select an audio file."
        }), 400

    if not allowed_file(audio.filename):
        return jsonify({
            "error": "Please upload a WAV audio file."
        }), 400

    temp_path = None

    try:

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".wav"
        ) as temp:

            audio.save(temp.name)
            temp_path = temp.name

        result = analyze_wav(temp_path)

        result["message"] = "Audio analyzed successfully."

        return jsonify(result)

    except wave.Error:

        return jsonify({
            "error": "The uploaded file is not a valid WAV file."
        }), 400

    except Exception as error:

        return jsonify({
            "error": f"Analysis failed: {str(error)}"
        }), 500

    finally:

        if temp_path and os.path.exists(temp_path):
            os.remove(temp_path)


@app.errorhandler(413)
def file_too_large(error):

    return jsonify({
        "error": "File is too large. Maximum size is 25 MB."
    }), 413


if __name__ == "__main__":
    app.run(debug=True)
