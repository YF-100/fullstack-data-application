from flask import Flask, render_template
import os, requests

app = Flask(__name__)

# API URL points to the service name and container port in docker-compose
API_URL = os.getenv("API_URL", "http://api:5001")

@app.context_processor
def utility_processor():
    def request_api():
        try:
            resp = requests.get(API_URL, timeout=5)
            resp.raise_for_status()
            return resp.text
        except Exception as e:
            return f"Error contacting API: {e}"
    return dict(request_api=request_api)

@app.route("/")
def hello():
    return render_template("index.html")
