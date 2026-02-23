
from flask import Flask, request, jsonify

app = Flask(__name__)
inbox = []

@app.route("/a2a/send", methods=["POST"])
def send():
    data = request.get_json()
    inbox.append(data)
    return jsonify({"status": "received"})

@app.route("/a2a/process", methods=["GET"])
def process():
    responses = []
    while inbox:
        msg = inbox.pop(0)
        responses.append({
            'from': 'AgentHTTP',
            'to': msg.get('from', 'unknown'),
            'content': f"Received: {msg.get('content', '')}"
        })
    return jsonify(responses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
