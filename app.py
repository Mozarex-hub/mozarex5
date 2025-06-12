from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

def roll_dice():
    return random.randint(1, 6)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/roll")
def roll():
    dice_value = roll_dice()
    return jsonify({"dice_value": dice_value})

@app.route("/results/<int:dice_value>")
def results(dice_value):
    return render_template("results.html", dice_value=dice_value)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
