from flask import Flask, request, jsonify
import threading

app = Flask(__name__)


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response


status_flag = None
latest_lyrics = ""


def reset_status():
    global status_flag
    status_flag = None


@app.route("/lyrics", methods=["POST"])
def lyrics():
    data = request.get_json(force=True)
    print("\n--- LYRICS ---++\n")
    print(data["lyrics"])
    global latest_lyrics
    latest_lyrics = data["lyrics"]
    return jsonify(ok=True)


@app.route("/status", methods=["POST"])
def status():
    global status_flag
    data = request.get_json(force=True)
    status_flag = data.get("status")
    if status_flag == "force":
        threading.Timer(1.5, reset_status).start()
    return jsonify(ok=True)


@app.route("/get_status", methods=["GET"])
def get_status():
    global status_flag
    response = {"status": status_flag or ""}
    return jsonify(response)


@app.route("/get_lyrics", methods=["GET"])
def get_lyrics():
    global latest_lyrics
    return jsonify({"lyrics": latest_lyrics})


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
