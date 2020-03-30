from flask import Flask, request, jsonify
from flask_cors import cross_origin
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return "Find out the status of a website"

@cross_origin()
@app.route("/api", methods=['GET', 'POST'])
def api():
    url = None
    if request.method == "GET":
        url = request.args.get("url")
    else:
        url = request.form.get('url')
    if url:
        res = requests.get(url)
        if res.ok:
            return jsonify({
                "status": "true"
            })
        else:
            return jsonify({
                "status": "false"
            })
    else:
        return jsonify({
            "status": "No url was passed"
        })


if __name__ == "__main__":
    app.run(host='0.0.0.0')