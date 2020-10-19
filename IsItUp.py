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
    print(url)
    if url:
        try:
            res = requests.head(url, timeout=5)
            status_code = res.status_code
            if res.ok:
                return jsonify({
                    "status": "yes"
                })
            elif res.status_code < 400:
                return jsonify({
                    "status": "redirect"
                })
            else:
                n = requests.status_codes._codes[status_code][0].replace("_", " ")
                status = "%d: %s"%(status_code, n)
                return jsonify({
                    "status": status
                })
        except Exception as e:
            return jsonify({
                "status": "Error"
            }) 
    else:
        return jsonify({
            "status": "No url was passed"
        })


if __name__ == "__main__":
    app.run(host='0.0.0.0')