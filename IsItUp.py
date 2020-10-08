from flask import Flask, request, jsonify
from flask_cors import cross_origin
import requests

app = Flask(__name__)

@app.route("/isitup")
def index():
    return "Find out the status of a website"

@app.route("/isitup/api", methods=['GET', 'POST'])
@cross_origin()
def api():
    url = None
    if request.method == "GET":
        url = request.args.get("url")
    else:
        url = request.form.get('url')
    if url:
        try:
            res = requests.get(url, timeout=30)
            if res.ok:
                return jsonify({
                    "status": "yes"
                })
            elif res.status_code < 400:
                return jsonify({
                    "status": "redirect"
                })
            else:
                return jsonify({
                    "status": res.status_code
                })
        except Exception as e:
            return jsonify({
                "status": str(e)
            }) 
    else:
        return jsonify({
            "status": "No url was passed"
        })


if __name__ == "__main__":
    app.run(host='0.0.0.0')