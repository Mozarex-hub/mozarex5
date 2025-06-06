import os
from flask import Flask, request, render_template_string

app = Flask(__name__, static_url_path='/static', static_folder='static')

@app.route("/", methods=["GET", "POST"])
def home():
    return "<h1>Welcome to Lifespan Estimator by MOZAREX™</h1>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
