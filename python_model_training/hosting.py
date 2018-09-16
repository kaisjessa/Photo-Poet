from flask import Flask, request
from flask_cors import CORS
import subprocess, json, traceback

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ["POST"])
def serveRoot():
    try:
        data = json.loads(request.data)
        return subprocess.check_output(["python3", "model_testing.py", data["keyword"]])
    except e:
        return traceback.format_exc()

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
